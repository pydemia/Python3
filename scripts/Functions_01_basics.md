[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)

---
# Functions

## Defining Functions

A **Fuction** has 2 steps;_Define_ & _Call_.
It operates when it is _called_.

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

* Arguments

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
```python
def adder(srt=string, num1=a, num2=b)
    print(srt, ': ', a + b)

adder(num1=4, str='Result', num2=3)
#'Result :  7'
```

# Data Structure

* [words](#words)





---
## words
words

### words

### Operation
 
```python
codes
```



[↑ Up to the Top](#data-structure)





---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)


