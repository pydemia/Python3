[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)


---

# Modules & Packages

* [Modules](#modules)  
* [Packages](#packages)


```python
import [Package]
import [Package] as [alias]

from [Package] import [Module]
from [Package] import *
from [Package] import [Module] as [alias] 
from [Package] import [Module1], [Module2] as [alias1], [alias2] 

```


---
## Basic ```.py``` Program
It's just files written in python. You can easily build a time-printing program like this:
```python
from datetime import datetime
print( datetime.time() )
```
after saving it;```timeprinter.py``` , execute this in console:
```sh
python timeprinter.py
```

You can check the time in console for now!



---
## Modules

```Modules``` are ```.py``` files containing **_Variables, Methods(Functions), Classes, etc._** It improve **_Reusability_** and **_Productivity_** in Python. You can re-use the methods by using ```import``` Statements.  

Let's build a basic calculator```calculator.py```:
```python
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def div(a, b):
    return a / b
def mul(a, b):
    return a * b
```

In ```PYTHONPATH/lib```, there are a lot of modules you can import. Put ```calculator.py``` in this path and load it using ```import```.   
```python
import calculator

calculator.minus(3, 1) # 2
```

The name ```calculator``` is too long. You can use **_Functions_** in ```calculator.py``` with its **_alias_**, ```cc``` or whatever you want.
```python
import calculator as cc
cc.plus(1, 2) # 3
cc.mul(3, 4)  # 12
```

If you only want to import ```div``` **_Function_** in ```calculator.py```:
```python
from calculator import plus as pp

pp(1,3) # 4
```

> Actually, Python searches files to import in sys.path, which is a standard module. you can see & edit pathes. This is an example:
```python
import sys
for directory in sys.path:
    print(directory)
```



---
## Packages

```Packages``` can be defined that contain one or more ```modules```.  If you want to get the result of ```plus``` **_Function_** with ```integer``` only, you can build two ```modules``` in one ```package```.  Let's make a ```operators``` directory, and put ```int_operators.py``` & ```float_operators.py``` under that directory:  

This is ```float_operators.py```  

```python
def plus(a, b):
    return int(a + b)
def minus(a, b):
    return int(a - b)
def div(a, b):
    return int(a / b)
def mul(a, b):
    return int(a * b)
```

and this is ```float_operators.py```  
```python
def plus(a, b):
    return float(a + b)
def minus(a, b):
    return float(a - b)
def div(a, b):
    return float(a / b)
def mul(a, b):
    return float(a * b)
```


To build a ```Package```, ```operators``` directory should have ```__init__.py```. It can be empty.  Python consider the directories have ```__init__.py``` as ```Packages```.  
Now you can import this ```package```.
```python
from operators import int_operators, float_operators as iop, fop

iop.div(2, 3) # 0
fop.div(2, 3) # 0.66666666666666
```
It's done!


[↑ Up to the Top](#modules-&-packages)


---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)
