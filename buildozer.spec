[app]
title = AviatorPredictor
package.name = aviatorpredictor
package.domain = org.nikuela
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pillow,pytesseract,matplotlib,certifi,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.api = 33
android.minapi = 21
android.archs = armeabi-v7a,arm64-v8a
android.ndk = 25b
# 🚫 ¡NO pongas ndk_path! Eso rompe builds en GitHub Linux

android.accept_sdk_license = True
android.permissions = INTERNET

buildozer_version = 1.5.0
