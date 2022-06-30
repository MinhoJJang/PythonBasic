# Part 1 정리

## 1장

### Python 설치

ubuntu 20.04 에서는 단순히 bash를 통해 python을 다운받을 수 있다.

[리눅스 Python 설치 방법](https://hiseon.me/python/linux-python-install/)

### turtle graphics 관련 오류

예제소스의 turtle_graphic.py 파일을 실행하자 아래와 같은 오류가 발생했다.

```
cd /home/mhj/gitRepo/PythonBasic ; /usr/bin/env /bin/python3 /home/mhj/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 35513 -- /home/mhj/gitRepo/PythonBasic/Part_1/1장/예제소스/1장/turtle_graphic.py
Traceback (most recent call last):
  File "/home/mhj/gitRepo/PythonBasic/Part_1/1장/예제소스/1장/turtle_graphic.py", line 2, in <module>
    import turtle
  File "/usr/lib/python3.8/turtle.py", line 107, in <module>
    import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'
```

`ModuleNotFoundError: No module named 'tkinter'` tkinter이라는 모듈이 없다고 하는 것 같으니 설치해주면 될 것 같다. 구글링을 통해 해결하였다.

[[Error Log]Python: No module named \_tkinter에 관한 이슈](https://ooeunz.tistory.com/23)

### Pycharm 설치

Pycharm은 마치 자바의 Eclipse 와 같은, Python을 위한 전용 툴이다. 해당 전용 사이트에서 다운받으면 된다.

다운받으면 tar.gz파일로 다운받게 되는데, 이때 설치하고싶은 폴더에 해당 파일을 압축해제한 뒤, 아래 README를 참고하여 설치하였다.

```
PyCharm

INSTALLATION INSTRUCTIONS
===============================================================================

  1. Unpack the PyCharm distribution archive that you downloaded
     where you wish to install the program. We will refer to this
     location as your {installation home}.

  2. To start the application, open a console, cd into "{installation home}/bin" and type:

       ./pycharm.sh

     This will initialize various configuration files in the configuration directory:
     ~/.config/JetBrains/PyCharmCE2022.1.

  3. [OPTIONAL] Add "{installation home}/bin" to your PATH environment
     variable so that you can start PyCharm from any directory.

  4. [OPTIONAL] To adjust the value of the JVM heap size, create a file pycharm.vmoptions
     (or pycharm64.vmoptions if using a 64-bit JDK) in the configuration directory
     and set the -Xms and -Xmx parameters. To see how to do this,
     you can reference the vmoptions file under "{installation home}/bin" as a model
     but do not modify it, add your options to the new file.

  [OPTIONAL] Change the location of the "config" and "system" directories
  ------------------------------------------------------------------------------

  By default, PyCharm stores all your settings in the
  ~/.config/JetBrains/PyCharmCE2022.1 directory
  and uses ~/.local/share/JetBrains/PyCharmCE2022.1 as a data cache.
  To change the location of these directories:

  1. Open a console and cd into ~/.config/JetBrains/PyCharmCE2022.1

  2. Create a file idea.properties and set the idea.system.path and idea.config.path variables, for example:

     idea.system.path=~/custom/system
     idea.config.path=~/custom/config

  NOTE: Store the data cache ("system" directory) on a disk with at least 1 GB of free space.


Enjoy!

-PyCharm Development Team
```

아래 설정을 통해 작업표시줄에서 즉시 Pycharm에 접근할 수 있도록 세팅하였다.

![pycharm setting](./img/pycharm.png)
