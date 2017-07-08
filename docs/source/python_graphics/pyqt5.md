# PyQt5

`PyQt5` is not compatible with `PyQt4` 
For example, All Widget stuffs are separated to independent Modules from each modules.
`QtWidgets` is splitted from `QtGui`, like `QtWebKitWidgets` does from `QtWebKit`.

## Installation

## Tools

### Qt Designer for `PyQt5`

```sh


sudo apt-get install python3-pyqt5 python3-pyqt5.qtsql qttools5-dev-tools
which designer
designer
```

### Create Shorcut
```sh
sudo vim /usr/share/applications/qtdesigner.desktop
```

```vim
[Desktop Entry]
Type=Application
Name=Qt Designer
GenericName=Qt Designer
Comment=PyQt5 Design Tool - Python3
TryExec=designer
Exec=designer
Categories=Development;Science;IDE;Qt;
Icon=QtProject-qtcreator
Terminal=false
StartupNotify=true

```
Then reboot.Done.


![qt creator](https://github.com/pydemia/Python3/blob/master/scripts/python_graphics/qt-designer.png?raw=True)



### Convert `.ui` file to `.py` file

```sh
pyuic5 -x input.ui -o output.py
```
