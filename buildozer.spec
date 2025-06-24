[app]
# (str) Título de tu aplicación
title = Aviator Predictor

# (str) Nombre del paquete
package.name = aviatorpredictor

# (str) Dominio del paquete (usado para bundleid en iOS)
package.domain = com.nikuela

# (str) Código fuente de tu aplicación principal
source.dir = .

# (str) Archivo principal de tu aplicación
source.main = main.py

# (list) Archivos fuente a incluir (dejar vacío para incluir todos)
source.include_exts = py,png,jpg,kv,atlas

# (str) Versión de la aplicación
version = 0.1

# (list) Dependencias de la aplicación
# Separadas por comas, ej: requirements = python3,kivy
requirements = python3,kivy

# (str) Icono de la aplicación
#icon.filename = %(source.dir)s/data/icon.png

# (str) Arquitecturas soportadas
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicar si la aplicación debe estar en pantalla completa
fullscreen = 0

[buildozer]
# (int) Nivel de log (0 = solo errores y advertencias, 1 = info, 2 = debug)
log_level = 2

# (int) Mostrar advertencias usando el logger de Python
warn_on_root = 1

[android]
# (int) Target Android API
android.api = 33

# (int) Minimum API que tu APK soportará
android.minapi = 21

# (str) Android NDK version a usar
android.ndk = 25.2.9519653

# (str) Android SDK directory (si está automáticamente detectado, puedes omitir esto)
#android.sdk_path = 

# (str) Android NDK directory (si está automáticamente detectado, puedes omitir esto)
#android.ndk_path = 

# (bool) Usar --private data storage (True) o --dir public storage (False)
android.private_storage = True

# (str) Formato del APK, 'debug' o 'release'
android.release = debug

# (str) python-for-android git clone directory
#android.p4a_dir = 

# (str) python-for-android branch
#android.p4a_branch = master

# (str) python-for-android git clone recursive
#android.p4a_clone_from_git_recursive = True

# (str) Bootstrap a usar para android builds
android.bootstrap = sdl2

# (list) Permisos
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Orientación
orientation = portrait

# (bool) Habilitar AndroidX
android.enable_androidx = True

[buildozer:debug]
# (str) Archivo de keystore para signing de debug
#android.debug_keystore = ~/.android/debug.keystore
