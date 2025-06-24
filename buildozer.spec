name: Build APK
on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repo
      uses: actions/checkout@v4
      
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
        
    - name: Cache pip dependencies
      uses: actions/cache@v4
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
          
    - name: Cache Android SDK
      uses: actions/cache@v4
      with:
        path: ~/android-sdk
        key: ${{ runner.os }}-android-sdk-${{ hashFiles('buildozer.spec') }}
        restore-keys: |
          ${{ runner.os }}-android-sdk-
    
    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          zip unzip openjdk-17-jdk ant \
          python3-pip libffi-dev libssl-dev \
          libbz2-dev libsqlite3-dev libncurses5-dev \
          libncursesw5-dev liblzma-dev tk-dev \
          git autoconf libtool pkg-config \
          zlib1g-dev
    
    - name: Set up Android SDK
      run: |
        # Crear directorio para Android SDK
        mkdir -p $HOME/android-sdk/cmdline-tools
        cd $HOME/android-sdk/cmdline-tools
        
        # Descargar command line tools
        wget -q https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip -O tools.zip
        unzip -q tools.zip
        mv cmdline-tools latest
        
        # Configurar variables de entorno para este paso
        export ANDROID_SDK_ROOT=$HOME/android-sdk
        export PATH=$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$PATH
        
        # Aceptar licencias e instalar componentes
        yes | sdkmanager --licenses >/dev/null 2>&1
        sdkmanager --sdk_root=$ANDROID_SDK_ROOT \
          "platform-tools" \
          "platforms;android-33" \
          "build-tools;33.0.2" \
          "ndk;25.2.9519653" \
          "cmake;3.22.1"
    
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip wheel setuptools
        pip install cython==0.29.36
        pip install buildozer
        pip install python-for-android
        pip install colorama appdirs sh jinja2 six
        # Si tienes requirements.txt, descomenta la siguiente línea
        # pip install -r requirements.txt
    
    - name: Set environment variables
      run: |
        echo "ANDROID_SDK_ROOT=$HOME/android-sdk" >> $GITHUB_ENV
        echo "ANDROID_NDK_ROOT=$HOME/android-sdk/ndk/25.2.9519653" >> $GITHUB_ENV
        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64" >> $GITHUB_ENV
        echo "$HOME/android-sdk/platform-tools" >> $GITHUB_PATH
        echo "$HOME/android-sdk/build-tools/33.0.2" >> $GITHUB_PATH
        echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH
    
    - name: Initialize Buildozer
      run: |        
        # Crear directorios necesarios
        mkdir -p ~/.buildozer/android/platform
        mkdir -p .buildozer/android/platform
        
        # Configurar permisos
        chmod -R 755 ~/.buildozer || true
        chmod -R 755 .buildozer || true
        
        # Limpiar cache previo si existe
        buildozer android clean || true
    
    - name: Build APK
      run: |
        # Ejecutar build con más verbose para debug
        buildozer android debug --verbose
        
        # Verificar que el APK se creó
        if [ ! -f bin/*.apk ]; then
          echo "Error: No se encontró el APK generado"
          echo "Contenido del directorio actual:"
          ls -la
          echo "Contenido del directorio bin/ (si existe):"
          ls -la bin/ || echo "Directorio bin/ no existe"
          echo "Contenido del directorio .buildozer:"
          find .buildozer -name "*.apk" -type f || echo "No se encontraron APKs en .buildozer"
          exit 1
        fi
    
    - name: Upload APK artifact
      uses: actions/upload-artifact@v4
      if: success()
      with:
        name: aviator-predictor-apk
        path: bin/*.apk
        retention-days: 30
        
    - name: Upload build logs
      uses: actions/upload-artifact@v4
      if: failure()
      with:
        name: build-logs
        path: |
          .buildozer/
          *.log
        retention-days: 7
