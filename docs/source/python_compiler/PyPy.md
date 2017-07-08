# PyPy

A Python Compiler built in Python.

## Installation

You can download [here](http://pypy.org/download.html)
(I got `Python 3.5.3 compatible PyPy3.5 v5.8`)

```sh
tar xvfj pypy3-v5.8.0-linux64.tar.bz2
ln -s pypy3-v5.8.0-linux64 pypy3
```

Set `PATH`:
```sh
vim ~/.bashrc
```

```vim

# PyPy PATH
export PATH="$APP_PATH/pypy3/bin:PATH"
export PYPY_PATH="$APP_PATH/pypy3"

```

## Run

```console
pypy3

Python 3.5.3 (a39af0be3a22, Jun 05 2017, 20:18:00)
[PyPy 5.8.0-beta0 with GCC 6.2.0 20160901] on linux
Type "help", "copyright", "credits" or "license" for more information.
And now for something completely different: ``Is rigobot around when the
universe ceases to exist?''
>>>> 

```
