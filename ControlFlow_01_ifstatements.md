[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)


# Control Flow Statements

* [Conditions](#conditions)
* [if statememts](#words)
* [for statements](#words)
* [while statements](#words)


---
## Conditions
An operation returns boolean(True or False)

* Comparison Opeators
| Operator | Description |
| :------: | :---------- |
| == | Equal to |
| != | NOT Equal to |
| <  | Less than |
| >  | Greater than |
| <= | Less than or Equal to |
| >= | Greater than or Equal to |
| in | Membership |

Chaining Comparison is supported in Python
```python
x = 5
#---------#
3 < x < 6
#---------#
True
```

* Boolean Operator
| Operator | Description |
| :------: | :---------- |
| and(&) | Equal to |
| or(|) | NOT Equal to |
| not(!)  | Less than |

Comparison Operator **is PRIOR to** Boolean Operator
```python
x = 5
#--------------#
3< x and x < 6
#--------------#
True
```

* Other False Type
| Objects | Description |
| :-----: | :---------- |
| null | None |
| int 0 | 0 |
| float 0 | 0.0 |
| an empty string | "" |
| an empty list | [] |
| an empty tuple | () |
| an empty dict | {} |
| an empty set | set() |

---
## If Statements
A Condition Statements

### if
* Code Structure
```python
condition = True
if condition:
    operation
```

* Example
```python
x = 3
#------------------#
if x < 5:
    print(x)
#------------------#
3


#------------------#
if x > 5:
    print(x)
#------------------#
Nothing is printed
```


### if-else
```python
condition = True
if condition:
    operation1
else:
    operation2
```

* Example
```python
x = 3
#------------------#
if x < 0:
    print("This number is negative!")
else :
    print("This number is not negative!")
#------------------#
"This number is not negative!"
```

### if-elif-else(multiple conditions)
```python
condition = True
if condition1:
    operation1
elif condition2:
    operation2
else:
    operation3
```

* Example
```python
x = 0
#------------------#
if x < 0:
    print("This number is negative!")
elif x == 0:
    print("This number is equal to Zero!")
else :
    print("This number is positive!")
#------------------#
"This number is equal to Zero!"
```



```

### words

### Operation
 
```python
codes
```



[↑ Up to the Top](#data-structure)


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

