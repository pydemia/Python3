[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)

---
# Basic Functions

---
## Defining Functions

A **Fuction** has 2 steps;   _Define_ & _Call_ .  
It operates when it is _called_.



### ```def ``` Statements

```python
# Define
def func_name():
    operation

# Call
func_name()
```

* Example
```python
def printer():
    print("Python!")

printer()
#'Python!'
```



### ```return``` Statements

It returns the result object of a _Fcuntion_ When the _Function_ is called.  
Using ```return``` can assign the result of a _Function_ as an _object_.

Look at the difference between ```print``` and ```return```

With ```print```, it just prints the result.
```python
def adder(a, b):
    print(a + b)

res = adder(1, 2)
#3 (print operation)
res
#Nothing is shown!
```

With ```return``` Statements:
```python
def adder(a, b):
    return a + b

res = adder(1, 2)
#Nothing is shown, but assignment is done!
res
#3
```





---
## Local and Global Variables

When Using a _Function_, the variables inside of the _Function_ and ones outside of the _Function_ are separate.  

_Inside of Objects like Classes or Functions_ are called **_Local Environments_**,  
and _Outside of Objects_ is called **_Global Environment_**.  

The variables belong to **_Local Environments_** are called **_Local Variables_**,  
and the variables belong to **_Global Environment_** are called **_Global Variables_**.  

**_Local Variables_** cannot affected to **_Global Variables_**
```python
x = 2        # 'x' is a global variable.
def funct():
    x = 10   # This 'x' is a local variable.
    print(x)

funct()
10          # It's about the local.

x
2           # It's about the global.
```


But in Local(in this case, inside of Functions), you can use Global Variables.  
This way is _**not recommended_** because operations in the local environments get affected to the **_Global Environment_** and throw _Errors & Exceptions_, despite Local operations are **CORRECT**!.  
_That's why we should use **Arguments**._

```python
x = 2        # 'x' is a global variable.
def funct():
    print(x)
```
funct()
2           # Local 'x' is not defined: then it refers to Global.
```



### ```global``` Statements

To change **_Global Variables_** in **_Local Environments_**, use ```global``` Statements.  
```python
x = 2        # 'x' is a global variable.
def funct():
    global x # For now, we use this 'x' as a global variable.
    x = 10   # Assign 10 to 'x' in the global environment.
    print(x)

funct()
#10

x
#10
```




---
## Arguments

A **Function** can have _arguments_.
```python
def adder(a, b):
    return(a + b)

adder(1, 2)
#3
```

Using _arguments_ should be careful, because of its **data type**.  
If you don't you would encounter many _Errors_ & _Exceptions_.
```python
adder('q', 2)
#Trackback (most recent call last):'
#TypeError: Can't convert 'int' object to str implicitly
```





---
### Positional Arguments

The way to use _arguments_ depending on its **order**.
```python
def adder(string, num1, num2):
    print(string, ': ', num1 + num2)

adder('Result', 2, 3)
#'Result :  5'
```




---
### Keyword Arguments

The way to use _arguments_ depending on its keyword(parameter).(Don't need to keep _arguments_ in order!)  
When using _Keyword Arguments_, you can set default values.  
The default values should be **_Constants_**  
```python
def adder(srt=string, num1=1, num2=2):
    print(srt, ': ', num1 + num2)

adder(num1=4, str='Result')
#'Result :  6'
```

**_Keyword Arguments_** should be defined behind **_Positional Arguments_**.
This is correct:
```python
def func(a, b=1):
```
The following is wrong:
```python
def func(a=1, b):
```




---
### Arbitrary Arguments Lists

Using **_\*_**, you can express variable numbers of **_Positional Arguments_**.  
At this time, ```*args```are gathered as a **_Tuple_**.  
It should be the end of the **_Positional Arguments_** lists.

* Example: ```*args```

```python
def printer(num1, num2, *args):
    print('num1:', num1)
    print('num2:', num2)
    print(args)

printer(2, 3, 4, 5, 7, 24)
num1: 2
num2: 3
(4, 5, 7, 24)   # a tuple
```

Using **_\*\*_**, you can express variable numbers of **_Keyword Arguments_**.  
At this time, ```*args```are gathered as a **_Dictionary_**.  
It should be the end of the **_Keword Arguments_** lists.

* Example: ```**kwargs```

```python
def printer(num1, num2=11, **args):
    print('num1:', num1)
    print('num2:', num2)
    print(kwargs)

printer(2, num2=4, num7=5, num8=7, num9=24)
num1: 2
num2: 4
{'num8': 7, 'num9': 24, 'num7': 5)   # a dict
```

* Order of Arguments: ```(arg, *args, kwarg, **kwargs)```

```python
def printer(num1, num2=11, **args):
    print('num1:', num1)
    print(args)
    print('num2:', num2)
    print(kwargs)

printer(1, 2, 3, num2=4, num7=5, num8=7, num9=24)
num1: 1
(2, 3)                              # a tuple
num2: 4
{'num8': 7, 'num9': 24, 'num7': 5)  # a dict
```




---
## Docstrings

For _Readability_, You can attach **_Documentation Strings_**.  
Just put the strings at the beginning of the function body; the first line of it!  


```python
def adder(a, b):
    'This function operates addition.'
    return(a + b)

adder(1, 2)
```

You can make multilined-Docstrings.
```python
def adder(a, b):
    '''
    This function
    operates
    addition.
    '''
    return(a + b)
```

**_Docstrings doesn't appear when the function is called.
```python
adder(1, 2)
3
```

To show **_Docstrings_**(if it exists), call the ```help()``` function.
```python
help(adder)
Help on function adder in module __main__:

adder(a, b)
    This function operates addition.
```

To show the raw **_Docstrings_**, call the ```__doc__``` variable.  
It is the internal name of **_Docstrings_** within the function.

```python
adder.__doc__
'This function operates addition.'

print(adder.__doc__)
'This function operates addition.'
```

[↑ Up to the Top](#basics-on-functions)

---
## Errors and Exceptions

### Errors
### Exceptions
### Clean-up Actions


[↑ Up to the Top](#errors-and-exceptions)



---

[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)


