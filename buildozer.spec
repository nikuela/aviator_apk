[app]
title = AviatorPredictor
package.name = aviatorpredictor
package.domain = org.nikuela
source.dir = .
version = 0.1
requirements = python3,kivy,pillow,pytesseract,matplotlib,certifi,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app/android]
android.api = 33
android.minapi = 21
android.permissions = INTERNET,CAMERA
android.archs = armeabi-v7a,arm64-v8a
