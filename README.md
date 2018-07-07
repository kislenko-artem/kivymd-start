## Kivy Сборка под  Docker (python 2.7)

`ВАЖНО!` сборку осуществлять внутри папки kivymd-start

* `docker build -t kivymd .`
* `docker run -it -v ${PWD}:/buildozer/ kivymd buildozer --verbose android debug`

## Отладка (android)

После сборки в папке проекта появится файл-apk. Его следует загрузить в телефон.

1. Включаем на телефоне [режим разработчика](http://androidmir.org/android/4901/)
2. Загружаем вам apk в телефон `adb install bin/KivyMD-0.1-debug.apk`
3. Смотрим логи `adb logcat | grep python` вместе с этим запускаем приложение на телефоне,
вместо реального телефона можно использовать эмулятор.

Буду рад любой обратной связи.
