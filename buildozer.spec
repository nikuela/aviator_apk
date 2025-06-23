[app]
title = MiAppEjemplo
package.name = miappejemplo
package.domain = org.tudominio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

android.api = 34
android.build_tools_version = 33.0.0

[buildozer]
log_level = 2

[android]
# sin build-tools ni ndk extras aquí
android.permissions = INTERNET
