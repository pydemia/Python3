[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)


---

# Classes

### Inheritance

Sometimes we don't satisfy with existing **_Classes_**. If **_Classes_** are too huge or complex to customize, modifying it is dangerous! We have a solution. **_Interitance_** can get things easier. _Child classes_(or _Subclasses_, _Derived classes_) inherited _Attributes_ and _Methods_ from their _Parent classes_(or _Superclasses_, _Base classes_). It's for **_Code reuse_** to improve productivity in Objective Oriented Programming. and more, _Child classes_ refer to _Parent classes_ when _Parent classes_ are modified. This is called **_Polymorphism_**.  

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


# Inheritance
class New_Membership(Membership):
    pass
```

```New_Membership``` **_Class_** is a specialized **_Class_** from ```Membership``` **_Class_**.  

You can do **_Multiple Inheritance_**  
```python
class DerivedClassName(Base1, Base2, Base3):
    {statement-1}
    .
    .
    .
    {statement-N}
```

### Method Overriding

You can re-define and modify existing _Methods_ derived from _Superclasses_ within _Subclasses_. That's **_Method Overriding_**.  

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
        
class New_Membership(Membership):
    def introduce(self):
        print("Hello, I'm a member of brand-new council,", self.fullname)
        
        
bruce = Membership('Bruce Lee')          # Instance bruce
bruce.introduce()                        # Hello, I'm a member, Bruce Lee

newbruce = NewMembership('Bruce Lee')    # Instance bruce
newbruce.introduce()                        # Hello, I'm a member of brand-new council, Bruce Lee
```

### ```super()``` Methods

To call the _Methods_ from _Superclass_ within _Subclass_, use ```super()``` _Methods_ in **_Subclasses_**!



```python
super().{superclass_method}
```


### [Iterables, Iterators and Generators](https://github.com/dawkiny/Python3/blob/master/scripts/ControlFlow_02_iter.md)



### [Coroutine](https://github.com/dawkiny/Python3/blob/master/scripts/ControlFlow_03_coroutine.md)

---



[↑ Up to the Top](#classes)


---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)
