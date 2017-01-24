[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/scripts/PythonProgramming.md)


# Classes

### Property

As different with _Java_, _Python_ doesn't support ```private``` Object property, because all properties & _Methods_ in _Python_ are ```public```! In _Python_, you just declare it in ```public``` first, and use ```property()``` or ```@property, @name.setter``` _decorator_ when you need to hide it to users.  

```property(get_name, set_name)```  
```python
class Namer():

    def __init__(self, input_name):
        self.hidden_name = input_name
        
    def get_name(self):
        print('the getter')
        return self.hidden_name
        
    def set_name(self):
        print('the setter')
        self.hidden_name = input_name
        
    name = property(get_name, set_name)    # Define two methods as property.

tmp = Namer('temp')
tmp.name             # the getter; 'temp'
tmp.get_name()       # the getter
tmp.set_name('txmp') # the setter; 'txmp'
tmp.name = 'ttmp'    # the setter; 'ttmp'
```




```@property(), @name.setter```
```python
class Namer():

    def __init__(self, input_name):
        self.hidden_name = input_name
        
    @property                              # for getter method
    def name(self):
        print('the getter')
        return self.hidden_name
        
    @name.setter                           # for setter method
    def name(self):
        print('the setter')
        self.hidden_name = input_name
        
    name = property(get_name, set_name)    # Define two methods as property.

tmp = Namer('temp')
tmp.name             # the getter; 'temp'
tmp.get_name()       # the getter
tmp.set_name('txmp') # the setter; 'txmp'
tmp.name = 'ttmp'    # the setter; 'ttmp'
```

```property``` can refer to calculated values!
```python
class circle():
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return 2 * self.radius

tmp = circle(7)
tmp.radius     # 7
tmp.diameter   # 14

tmp.radius = 5
tmp.diameter   # 10  # 'diameter' refered to the value of 'radius' and automatically changed! 

tmp.diameter = 4     # without 'setter property', it cannot be modified from outside. (read-only)
```


### Private Name Mangling

use **_DOUBLE UNDERSCORE_** naming like ```__init__```, to hide attributes from outside. Its _Mangling_.  

### Method Types

**_Instance Methods_** : _Methods_ have ```self``` as the first parameter. It valid & affect the its _Class_.  
**_Class Methods_** : _Methods_ have ```cls``` as the first parameter. It affect **_WHOLE CLASSES_** using ```@classmethod```.  
**_Static Methods_** : These _Methods_ have no parameter. It's just for _Classes_ itself and you don't need to generate _Objects_ to use this _Methods_. just use ```@staticmethod```


### Duck-typing

tbd

### Special Methods

tbd

### Composition and Aggregation

tbd

### Named-tuple
A _Subclass_ of **_Tuple_**. You can access its values with ```.name``` and ```[offset]```.



[↑ Up to the Top](#classes)



---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/scripts/PythonProgramming.md)
