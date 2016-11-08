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

* Boolean Operators

| Operator | Description |
| :------: | :---------- |
| and(&) | Equal to |
| or(|) | NOT Equal to |
| not(!)  | Less than |

Comparison Operator **is PRIOR to** Boolean Operator
```python
x = 5
#--------------#
3 < x and x < 6
#--------------#
True
```

* Other False Cases

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
Conditional Statements: Execute ONCE.

### if

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
#Nothing is printed
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
    print("'x' is negative!")
else :
    print("'x' is not negative!")
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
    print("'x' is negative!")
elif x == 0:
    print("'x' is equal to Zero!")
else :
    print("'x' is positive!")
#------------------#
"'x' is equal to Zero!"
```


### inner if(precising your conditions)

* Example
```python
x = -1
#------------------#
if x < 0:
    if x == -2
        print("x is -2")
    else:
        print("'x' is negative!")
elif x == 0:
    print("'x' is equal to Zero!")
else :
    print("'x' is positive!")
#------------------#
"This number is negative!"
```


---
## While Statements
Loop statements(Repeat while condition is True)


### while

```python
condition = True
while condition:
    operation
```

* Example
```python
x = 3
#------------------#
while x < 7:
    print(str(x) + " is less than 7!")
    x += 1
#------------------#
"'3' is less than 7!"
"'4' is less than 7!"
"'5' is less than 7!"
"'6' is less than 7!"
```

### break
```python
condition1 = True
while condition1:
    operation1
    if condition2:
        break
```

* Example
```python
x = 0
#-------------#
while True:
    x += 1
    if x == 4:
        break
    print (x)
#-------------#
1
2
3
```

### continue: jump to next
```python
condition1 = True
while condition1:
    operation1
    if condition2:
        continue
```

* Example
```python
x = 0
#-------------#
while x < 10:
    x += 1
    if x % 2 == 0:#if 'x' is even number 
        continue
    print (x)
#-------------#
1
3
5
7
9
```

### else: following break statements
```python
condition1 = True
while condition1:
    operation1
    if condition2:
        break
```

* Example
```python
x = 0
#-------------#
while True:
    x += 1
    if x == 4:
        break
    print (x)
#-------------#
1
2
3
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

