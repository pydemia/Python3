[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)

---
# Functions

## Defining Functions

A **Fuction** has 2 steps;_Define_ & _Call_.
It operates when it is _called_.

### ```python def ```
```python
# Define
def func_name():
    operation

# Call
func_name()
```

* Example
```python
def printer()
    print("Python!")

printer()
#'Python!'
```

### Arguments

A **Function** can have _arguments_.
```python
#-----------------#
def adder(a, b)
    return(a + b)
#-----------------#
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

## Positional Arguments

The way to use _arguments_ depending on its **order**.
```python
def adder(string, num1, num2)
    print(string, ': ', num1 + num2)

adder('Result', 2, 3)
#'Result :  5'
```

## Keyword Arguments

The way to use _arguments_ depending on its keyword(parameter).(Don't need to keep _arguments_ in order!)
When using _Keyword Arguments_, you can set default values.
The default values should be **_Constants_**
```python
def adder(srt=string, num1=1, num2=2)
    print(srt, ': ', num1 + num2)

adder(num1=4, str='Result')
#'Result :  6'
```

**_Keyword Arguments_** should be defined behind **_Positional Arguments_**.
This is correct:
```python
def func(a, b=1)
```
The following is wrong:
```python
def func(a=1, b)
```

[↑ Up to the Top](#data-structure)





---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)


