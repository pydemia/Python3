[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_advanced.md#advanced-python)


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

This contains the basics of Special Methods. More informations are [here].(https://github.com/pydemia/Python3/blob/master/scripts/python_programming/advanced/special_methods.md)

* **`__init__`** : **Do** something when a `instance` is **`initiated`**. _(cannot use `return` Statement)_
* **`__new__`** : **Do & Return** something when **`initiated`**. _(can use `return` Statement)_
* **`__str__`** : **Show** something when a `instance` is **`printed`**.
* **`__repr__`** : **Show** something when a `instance` is **`called` from console**.
* **`__call__`** : tbd
* **`__getitem__`** : Be able to **subset** & **slice** it.
* **`__setitem__`** : Be able to **replace** existing item.
* **`__iter__`** : tbd
* **`__next__`** : tbd
* **`__dir__`** : tbd
* **`__doc__`** : tbd
* **`__getattr__`**, **`__getattribute__`** : tbd
* **`__setattr__`** : tbd

```py
class myobject(object):
    
    def __init__(self, obj, name):
        
        # Check if listobj is list type OR just you can change it to list
        if not isinstance(obj, list):
            obj = list(obj)
        
        self.data = obj
        self.name = name
        #self.InitData(data)
    
    def __new__(cls, *args, **kwargs):
        #return super(myobject, cls).__new__(cls)
        return super().__new__(cls)
    
    def __str__(self):
        return str(self.data)
    
    #def __call__(self):
    #    print(self.name)
    #    print(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
        #return self.data
    
    #def __delitem__(self):
    #    pass
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return str(self.data)
```
   
```py
# Create a new instance : __init__, __new__
tmpls = [1,2,3]
myobj = myobject(tmpls, 'Test')

# Check attributes
myobj.data
myobj.name

# Type(Class)
type(myobj)


# print & str : __str__, __repr__
print(myobj)
str(myobj)
myobj

# Indexing : __getitem__
myobj[1]

# Replacing : __setitem__
myobj[2] = 4

# Container Size : __len__
len(myobj)
```


### Composition and Aggregation

tbd


[↑ Up to the Top](#classes)



---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_advanced.md#advanced-python)
