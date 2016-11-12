[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)


# Classes

## Basics on Classes

### Objects & Classes

* **Objects**  
Data(Variables, Attributes) or Codes(Functions, Methods)  
Objects are **_THE UNIQUE INSTANCE_** of something concrete.  

* **Classes**  
Number ```7```, String ```'keyboard'``` and Function ```adder``` are _Objects_, **Each of them represents something concrete**.  Number ```7``` represents An Attribute 'Number' _Seven_, Using **_Class_** ```int```.  
String ```keyboard``` represents An Attribute 'Word' _keyboard_, Using **_Class_** ```str```.  
and Function ```adder``` represents A Function 'Code' _adder', Using  **_Class_** ```function```.  

* **Methods**  
Classes have **_Methods_**. **_Methods_** are _Functions_ defined within **_Classes_**. For example, ```str``` **_Class_** has ```.find()``` or ```.upper()``` **_Methods_**.  
**These Methods are defined in** ```str``` **_Class_** **and called for some operation with its Attribute(Data)** _keyboard_.  

> In Object-Oriented Programming(**OOP**),  Attributes & Methods are hierarchically classificated into Classes.  
> **_Classes_** are sort of boxes, which is classificated by its usage.  
> (A steel box for heavy things, a paper box for books, and a plastic box for fishes or water thing.)  
> Like this, **Each** **_Classes_** **are defined & ready to deal with Data & Codes.**  
> With **_Instance_**, **_Classes_** are _instantiated_ and **_Objects_** that have some concrete things are generated.  



---
### Defining Classes  

* ```class``` Statements  
You can make **_Classes_** with ```class``` Statements.
```python
class Membership:
    pass
```
It's an empty **_Class_**. Like Functions, We can assign this **_Class_** and generate an **_Object_**.  
```python
someone = Membership()
someone
<__main__.Person object at 0x7fac781345f8> # An Object with __main__ Module, Person Class
```

* ```__init__``` Methods : Object Initialization  

Let's make another one.  

```python
class Membership:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hello, I'm a member,", self.name)

bruce = Membership('Bruce Lee')    # Instance bruce
bruce.introduce()                  # Hello, I'm a member, Bruce Lee
```
```__init__``` Methods is _called_ when A **_Class_** is _instantiated_!
```__init__``` Methods _initialize_ a UNIQUE **_Class_** from **_Classes_** Definition when **_Objects_** are _generated_.   

```self``` is the First Arguments refer to the **_Instance_** itself. It is invisible when ```bruce``` _Instance_ is generated(We delivered only one argument in ```Membership('Bruce Lee')```), but automatically delivered to Python Method.  

```__init___``` Method should have one Argument, which refer to the **_Instance_** itself. It should be the first Argument of ```__init___``` Method. The word 'Self' is _generally_ used and _highly recommended_ for its name.  
 
 
 
---
### Class Variables and Method Variables

Let's define a basic **_Class_**.  
```python
class Membership:
    count = 0
    def __init__(self, name):
        self.fullname = name
        Membership.count += 1
    def introduce(self):
        print("Hello, I'm a member,", self.fullname)
    def __del__(self):
        Membership.count -= 1

bruce = Membership('Bruce Lee')    # Instance bruce
bruce.introduce()                  # Hello, I'm a member, Bruce Lee
bruce.fullname                     # Bruce Lee
bruce.count                        # 1

paul = Membership('Paul Phoenix')  # Instance paul
paul.introduce()                   # Hello, I'm a member, Paul Phoenix
paul.fullname                      # Paul Phoenix
paul.count                         # 2

```

In ```Person()``` **_Classes_**, some **_Objects_** are defined.  

| Object | Description |
| :----: | :---------- |
| ```count``` | A _Class Variable_ |
| ```__init__``` | A _Method_ |  
| ```self``` | An _Argument_ refer to each **_Instance_** itself. |
| ```name``` | A _Local Variable_ within __init__ _Method_ |
| ```fullname``` | A _Instance Variable_(```self.fullname```) | 


_Class Variable_ is shared by all **_Instance_**.  
_Instance Variable_ should be unique to each **_Instance_**, not interrupting each other. 

```paul.fullname``` is a _Instance Variable_, so It has an _Unique_ name. ```paul.count``` is A _Class Variable_, so It has an _Shared_ number, 2.    



---
### Scopes and Namespaces  

As the previous case , you saw two kinds of _Variables_ have different _Value-sharing ranges_. This _ranges_ are named **_Namespaces_**, literally. It's the mapping between _Names_ and _Objects_, so **_Namespaces_** are mostly made of _Dictionaries_.  

To show the **_Namespaces_**, use ```__dict__``` Methods, which is the _Built-in Methods_.  
```python
bruce.__dict__ # {'name': 'Bruce Lee'}
paul.__dict__  # {'name': 'Paul Phoenix'}
Membership__dict__
# mappingproxy({'__weakref__': <attribute '__weakref__' of 'Membership' objects>, '__del__': <function Membership.__del__ at 0x7fe9da53f400>, 'count': 2, '__init__': <function Membership.__init__ at 0x7fe9da53f2f0>, '__dict__': <attribute '__dict__' of 'Membership' objects>, '__module__': '__main__', 'introduce': <function Membership.introduce at 0x7fe9da53f378>, '__doc__': None})
```
You can see ```name``` Variables are in the _Instance_ **_Namespaces_** and ```count``` Variable is in the _Class_ **_Namespace_**. When you call ```.count``` Variable from each _Instances_, Python searches it from _Instances_ first, and then from _Classes_ next. That's how ```paul.count``` returns ```2```.   


* ```global``` Statements  

* ```nonlocal``` Statements  

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

```



---
## Errors and Exceptions

### Errors
### Exceptions
### Clean-up Actions


## Advances in Classes

### Inheritance
### Iterables, Iterators and Generators
### Coroutine

---



[↑ Up to the Top](#data-structure)





---
## words​
4
# Data Structure
5
​
6
* [words](#words)
7
​
8
​
9
​
10
​
11
## Errors
12
​
13
## Exceptions
14
​
15
## Clean-up Actions
words

### words

### Operation
 
```python
codes
```



[↑ Up to the Top](#data-structure)





---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)
