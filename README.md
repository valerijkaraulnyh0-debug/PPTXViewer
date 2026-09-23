# PPTX Viewer — Android-приложение для просмотра PowerPoint

## Что это
Android-приложение на Kivy + python-pptx. Открывает .pptx файлы,
отображает слайды с текстом и картинками, навигация свайпом или кнопками.

## Структура проекта
- `main.py` — основное приложение
- `buildozer.spec` — конфигурация сборки APK

## Как собрать APK

### Вариант 1: На Linux (Ubuntu/Debian)
```bash
# Установить зависимости
sudo apt update
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool
pip3 install buildozer cython

# Перейти в папку проекта
cd PPTXViewer

# Собрать APK (первая сборка ~30-60 мин)
buildozer -v android debug

# Готовый APK
ls bin/*.apk
```

### Вариант 2: Через GitHub Actions (без Linux)
1. Загрузите проект на GitHub
2. Добавьте workflow из `.github/workflows/build.yml`
3. GitHub сам соберёт APK — скачайте из Artifacts

### Вариант 3: Через Docker
```bash
docker run --rm -v $(pwd):/home/user/hostcwd kivy/buildozer android debug
```

## Установка на телефон
```bash
# Через ADB
adb install bin/pptxviewer-1.0-arm64-v8a-debug.apk

# Или скопируйте APK на телефон и откройте
```

## Возможности
- Открытие .pptx файлов через системный диалог
- Отображение текста и изображений со слайдов
- Навигация: свайп влево/вправо или кнопки
- Ландшафтная ориентация

## Ограничения
- Нет рендеринга анимаций и переходов
- Нет поддержки встроенных видео и аудио
- Базовое форматирование текста (без точного позиционирования шрифтов)
- Не поддерживает .ppt (только .pptx)
