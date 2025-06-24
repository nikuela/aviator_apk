[app]
title = AviatorPredictor
package.name = aviatorpredictor
package.domain = org.nikuela

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pillow,pytesseract,matplotlib,certifi,requests

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = armeabi-v7a,arm64-v8a
android.permissions = INTERNET
android.ant_path = $HOME/ant
