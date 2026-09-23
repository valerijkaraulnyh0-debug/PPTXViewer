[app]

# Application metadata
title = PPTX Viewer
package.name = pptxviewer
package.domain = org.pptxviewer

source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,svg

version = 1.0

# Requirements
requirements = python3,kivy,python-pptx,Pillow,lxml,olefile,xlsxwriter

# Android configuration
orientation = landscape

# Fullscreen
fullscreen = 0

# Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# API
android.api = 31
android.minapi = 21

# NDK
android.ndk = 25b

# Build options
android.archs = arm64-v8a,armeabi-v7a

# Log level
log_level = 2

# Copy libs
android.add_src = 

# Presplash
presplash.filename = 

# Icon
icon.filename = 

# Deep link
android.allow_backup = True

[buildozer]

# Buildozer config
log_level = 2
warn_on_root = 1
