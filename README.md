## Kivy Сборка под  Docker (python 2.7)

`ВАЖНО!` сборку осуществлять внутри папки kivymd-start

* `docker build -t kivymd .`
* `docker run -t kivymd -v ${PWD}:/buildozer/ buildozer --verbose android release`

Буду рад любой обратной связи.
