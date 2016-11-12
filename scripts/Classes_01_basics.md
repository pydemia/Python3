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

```self``` is the First Arguments refer to the **_Instance_** itself.  
It is invisible when ```bruce``` _Instance_ is generated(We delivered only one argument in ```Membership('Bruce Lee')```), but automatically delivered to Python Method.  
```__init___``` Method should have one Argument, which refer to the **_Instance_** itself.
And this Argument should be the first Argument of ```__init___``` Method.  
The word 'Self' is _generally_ used and _highly recommended_ for its name.  
 

### Scopes & Namespaces

Let's define a basic **_Class_**.  
```python
class Membership:
    count = 0
    def __init__(self, name):
        self.name = name
        Membership.count += 1
    def introduce(self):
        print("Hello, I'm a member,", self.name)
    def __del__(self):
        Membership.count -= 1

bruce = Membership('Bruce Lee')    # Instance bruce
bruce.introduce()                  # Hello, I'm a member, Bruce Lee

paul = Membership('Paul Phoenix')  # Instance paul
paul.introduce()                   # Hello, I'm a member, Paul Phoenix

bruce.name
paul.name

```

In ```Person()``` **_Classes_**, some **_Objects_** are defined.  
* ```count``` Argument: A _Class Variable_
* ```__init__``` Method: A _Class Method_   
1. ```self``` Argument A _ 
2. ```name``` Argument: A _Local Variable_ within __init__ _Method_ 
3. ```name``` Argument = self.name: A _Instance Variable_  



먼저 매개 변수 name 을 넘겨 받는 init 메소드를 정의합니다(물론 self를 포함하여 정의합니다). 그리고, name 이라는 필드를 생성합니다. 이 때 두 다른 변수의 이름으로 'name' 이라는 동일한 이름을 지정해 주었다는 점에 주목하시기 바랍니다. 이것이 문제가 되지 않는 이유는 하나는 "self" 라 칭해지는 객체에 내장된 것으로써 self.name 의 형태로 사용되며 또 하나인 name 은 지역 변수를 의미하는 것으로 사용되기 때문입니다. 프로그램 상에서 각각을 완전하게 구분할 수 있으므로, 혼란이 일어나지 않습니다.

위 예제에서 가장 중요한 것은, 우리가 init 메소드를 직접 호출해 주지 않고 클래스로부터 인스턴스를 생성할 때 괄호 안에 인수를 함께 넘겨 주었다는 점입니다. 이 점이 이 메소드가 좀 특별하게 다뤄지는 이유입니다.

이제, sayHi 메소드에서처럼 객체 내부에서 self.name 필드를 사용할 수 있습니다.

앞서 클래스와 객체가 어떤 기능을 갖도록 하는 방법, 즉 메소드에 대해 설명했습니다. 이제 데이터의 경우 어떻게 하는지 배워봅시다. 데이터, 즉 필드는 일반적인 변수와 다를 것이 없으나 딱 한 가지, 그 클래스 혹은 객체의 네임스페이스 에 묶여 있다는 점이 다릅니다. 이것은 필드의 이름은 그 클래스 혹은 객체 내부에서만 의미가 있음을 의미합니다. 그래서 이것을 이름이 통용되는 공간이라고 하여 네임스페이스 라고 부릅니다.

필드 에는 두 종류가 있는데, 클래스 변수와 객체 변수입니다. 각각은 그것을 소유하고 있는 대상이 클래스인지 객체인지에 따라 구분됩니다.

클래스 변수 는 공유됩니다. 즉, 그 클래스로부터 생성된 모든 인스턴스들이 접근할 수 있습니다. 클래스 변수는 한 개만 존재하며 어떤 객체가 클래스 변수를 변경하면 모든 다른 인스턴스들에 변경 사항이 반영됩니다.

객체 변수 는 클래스로부터 생성된 각각의 객체/인스턴스에 속해 있는 변수입니다. 이 경우에는, 각각의 객체별로 객체 변수를 하나씩 따로 가지고 있으며, 서로 공유되지 않고 각 인스턴스에 존재하는 같은 이름의 필드끼리 서로 어떤 방식으로든 간섭되지 않습니다.

### Classes & Instances & Methods

Class Methods , Instance Methods  

## Errors & Exceptions

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
