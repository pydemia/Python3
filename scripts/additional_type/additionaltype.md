# Python Additional Type Object

## Built-in Libraries

### enum.Enum

```py
import enum
```

```py
class color(enum.Enum):
    
    red = 1
    green = 2
    blue = 3


class city(enum.Enum):
    
    seoul = 1
    tokyo = 2
    london = 3
    
```

Check items:
```py
aColor = color.red
bColor = color.green

aCity = city.seoul
bCity = city.tokyo


aColor.name  # 'red'
bCity.name  # 'tokyo'

bColor.value  # 2
aCity.value  # 1
```

Selection:
```py
color(1)  # <color.red: 1>
city['london']  # <city.london: 3>
```

Copy items (the first one is the original):
```py
class color(enum.Enum):
    
    red = 1
    green = 2
    blue = 3
    grey = 2


color.green  # <color.green: 2>  : Original
color.grey  # <color.green: 2> : Duplicated
```

Then, Unique Enum:
```py
@enum.unique
class color(enum.Enum):
    
    red = 1
    green = 2
    blue = 3
    grey = 2
```

the values of `enum.Enum` can be `str`:
```py
class strcity(enum.Enum):
    
    seoul = 'a'
    tokyo = 'b'
    london = 'c'

strcity('c')  # <strcity.london: 'c'>
```

`enum.IntEnum` (only `int` can be used as a value): 
```py
class intcity(enum.IntEnum):
    
    seoul = 1
    tokyo = 2
    london = 3

```

Comparison:
```py
color.red == color.red  # False
color.red is color.red  # True
color.red == color.blue  # False
color.red is not color.blue  # True
color.red < color.blue  # TypeError: unorderable types

color.red == 1  # False
```

But, the value of `enum.IntEnum ` can be compared (like `int`):
```py
intcity.seoul == 1  # True
```


### collections.namedtuple
A _Subclass_ of **_Tuple_**. You can access its values with ```.name``` and ```[offset]```.

