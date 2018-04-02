Минимальная конфигурация для старта приложения для Android с Kivy-md.

Требуется поддержка python2.7, к сожалению, собрать для python3 не получилось, не запускается apk на телефоне.

Сама сборка осуществляется через бульдозер:

`buildozer android debug deploy run`

При сборке может возникнуть ошибка:

`IOError: [Errno 2] No such file or directory: u'/home/kivy/Hello/.buildozer/android/platform/build/dists/myapp/build/outputs/apk/myapp-debug.apk'`

Решение описано здесь -> https://github.com/kivy/buildozer/issues/312

Буду рад любым комитам.
