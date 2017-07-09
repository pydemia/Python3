# What's new in Python 3.6


### PEP 498: Formatted string literals


```python
name = "Fred"
f"He said his name is {name}."

Out[]:
'He said his name is Fred.'

width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"  # nested fields

Out[]:
'result:      12.35'
```


### PEP 526: Syntax for variable annotations(related to PEP 484: Type hints)

It's useful when defining a function.


```py
def sayHello(name: str) -> str:
    return 'Hello, ' + name

sayHello(12)

# Traceback (most recent call last):
# 
#  File "<ipython-input-21-ebcad19ed18d>", line 1, in <module>
#     sayHello(12)
# 
#  File "<ipython-input-19-eb4e86d0b2ac>", line 2, in sayHello
#     return 'Hello, ' + name
#
# TypeError: must be str, not int

sayHello('12')

Out[]:
'Hello, 12'
```
```python
from typing import List
primes: List[int] = []
captain: str  # Note: no initial value!

from typing import Sequence, TypeVar
T = TypeVar('T')      # Declare type variable

def greeting(name: str) -> str:
    return 'Hello ' + name

class Starship:
    stats: Dict[str, int] = {}
```



### PEP 515: Underscores in Numeric Literals(!)


```python
1_000_000_000_000_000

Out[]:
1000000000000000

0x_FF_FF_FF_FF

Out[]:
4294967295

# Presentation Formatting
'{:_}'.format(1000000)          # '_' for thousands, 'd' for integer only
'1_000_000'
>>> '{:_x}'.format(0xFFFFFFFF)  # 'b', 'o', 'x', 'X' for integer presentation: 4 digits
'ffff_ffff'
```


### PEP 525: Asynchronous Generators(!)

You can use not only ```await``` & ```await```, but also ```await``` & ```yield``` For now!
```python
def func():            # a function
    return

def genfunc():         # a generator function
    yield

async def coro():      # a coroutine function
    await smth()

async def asyncgen():  # an asynchronous generator function
    await smth()
    yield 42


async def gen():
    try:
        await asyncio.sleep(0.1)
        yield 'hello'
    except ZeroDivisionError:
        await asyncio.sleep(0.2)
        yield 'world'

g = gen()
v = await g.asend(None)
print(v)                # Will print 'hello' after
                        # sleeping for 0.1 seconds.

v = await g.athrow(ZeroDivisionError)
print(v)                # Will print 'world' after
                        # sleeping 0.2 seconds.
```


### PEP 530: Asynchronous Comprehensions


```python
result = [i async for i in aiter() if i % 2]

result = [await fun() for fun in funcs if await condition()]
```


### PEP 487: Simpler customization of class creation( Add  ```__init_subclass__```)

```python
class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

class Plugin1(PluginBase):
    pass

class Plugin2(PluginBase):
    pass
```


### PEP 487: Descriptor Protocol Enhancements( Add ```__set_name__()```)
```python
class IntField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting integer in {self.name}')
        instance.__dict__[self.name] = value

    # this is the new initializer:
    def __set_name__(self, owner, name):
        self.name = name

class Model:
    int_field = IntField()
```


### PEP 519: Adding a file system path protocol( easy to use path strings)
```python
#--------------------------------------------------#
import pathlib
with open(pathlib.Path("README")) as f:
...     contents = f.read()
...

#--------------------------------------------------#
import os.path
os.path.splitext(pathlib.Path("some_file.txt"))
('some_file', '.txt')

os.path.join("/a/b", pathlib.Path("c"))
'/a/b/c'

#--------------------------------------------------#
import os
os.fspath(pathlib.Path("some_file.txt"))
'some_file.txt'
```


### PEP 529: Change Windows filesystem & console encoding to UTF-8
```python
sys.getfilesystemencoding()

Out:[] 
'utf-8'
```

### PEP 523: Adding a frame evaluation API to CPython

