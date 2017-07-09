[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)


---

# Control Flow

* [Conditionals](#conditions)
* [if Statememts](#if-statements)
* [while Statements](#while-statements)
* [for Statements](#for-statements)

---
## Conditionals

An operation returns boolean(True or False)

### Comparison Opeators

| Operator | Description              |
| :------: | :----------              |
| `==`     | Equal to                 |
| `!=`     | NOT Equal to             |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or Equal to    |
| `>=`     | Greater than or Equal to |

* Statements

| Statement | Description |
| :------: | :---------- |
| `is` | Same to |
| `not` | NOT Same to |
| `in` | Membership |


#### Difference between `==` and `is`  

`==` is the equality comparison.  
`is` is the identity comparison.

```py
a = 256
b = 256

a is b      # True
a == b      # True
```

That's weird. `a is b` should return `False` since `a` and `b` is not the same object.  
That's because integer 0 ~ 256 is internally pre-assigned for convenience.

```py
a = 257
b = 257

a is b      # False
a == b      # True
```
Now it works theoretically.

Chaining Comparison is supported in Python
```python
x = 5
#---------#
3 < x < 6
#---------#
True
```

### Boolean Operators

| Operator | Description |
| :------: | :---------- |
| `and` | Equal to |
| `or` | NOT Equal to |
| `not`  | Less than |


Comparison Operator **is PRIOR to** Boolean Operator
```python
x = 5
#--------------#
3 < x and x < 6
#--------------#
True
```

* The returned Values of `Boolean operators`  

```py
# and
print(True and 'OK')              # Ok
print(False and 'OK')             # False

print(True and 'OK' or 'NO')      # OK
print(False and 'OK' or 'No')     # No

# or
print(True and 'OK')              # True
print(False and 'OK')             # Ok

print(True or 'OK' or 'No')       # True 
print(False or 'OK' or 'No')      # OK
```

`and` :  
```py
def and(x, y):
    if x == False:
        return x
    else
        return y
```

`x` `and` `y` first evaluates `x`.
If `x` is `False`, its value is returned.
Otherwise, `y` is evaluated and the resulting value is returned.

* `or` :  
```py
def and(x, y):
    if x == True:
        return x
    else
        return y
```

The expression `x` `or` `y` first evaluates `x`.
If `x` is `True`, its value is returned.
Otherwise, `y` is evaluated and the resulting value is returned.

Note : Neither `and` nor `or` restrict the value and type they return to `False` and `True`, but rather return `the last evaluated argument`.


### Bitwise Operators

| Operator | Description         | Looks like    |
| :------: | :----------         | :------       |
| `&`      | bitwise `and`       | `x and y`     |
| `|`      | bitwise `or`        | `x or y`      |
| `~`      | bitwise `not`       | `not x`       |
| `^`      | bitwise `xor`       | ``      |
| `<<`     | bitwise right shift(1111 0000) | `x * (2**y)`  |
| `>>`     | bitwise left shift(0000 1111)  | `x //(2**y)`  |


#### Difference between `Bitwise Operators` and `Boolean Operators`

#### Case 1 : `&` and `and` (`|` and `or`)  
Comparison Operators can be operated with the same type.

```py
print(True & 'OK')
print(False | 'OK')

TypeError: unsupported operand type(s) for &: 'bool' and 'str'
```

```py
print(True and 'OK')     # Ok
print(False and 'OK')    # False
```




* Other False Cases

| Objects | Description |
| :-----: | :---------- |
| `null` | None |
| `int` 0 | 0 |
| `float` 0 | 0.0 |
| an empty string | "" |
| an empty list | [] |
| an empty tuple | () |
| an empty dict | {} |
| an empty set | set() |

[↑ Up to the Top](#control-flow-statements(conditionals-&-loops))


---
## if Statements

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

[↑ Up to the Top](#control-flow-statements(conditionals-&-loops))

---
## while Statements

Loop statements with conditions(Repeat while condition is True)


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
    print(str(x) + " is less than 7!")#str() for converting int to str
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
        operation_when_break#This line is not necessary
        break
```

* Example
```python
x = 0
#-------------#
while True:
    x += 1
    if x == 4:
        print(x
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

### else: with break statements(break or even)

```python
condition1 = True
while condition1:
    operation1
    if condition2:
        operation_when_break#This line is not necessary
        break
else:
    operation3
```

* Example
```python
x = [1, 3, 5, 7, 9]
ord = 0
#-------------#
while ord < len(x):
    num = x[ord]
    if num % 2 == 0:#if 'x' is even number
        print('An even number is detected!')
        break
    x += 1
    else: 
        print('There is no even number found!')
#-------------#
"There is no even number found!"
```

[↑ Up to the Top](#control-flow-statements(conditionals-&-loops))

---
## for Statements

Loop statements with Sequences(Iterate sequences)

### for

```python
for i in iterables:
    operation(with i or not)
```

* Example 1(with range( ))
```python
#-------------------#
for i in range(4):
    print(i)
#-------------------#
0
1
2
3#startswith 0, endswith 4-1 = 3(the last one is not used)
```

* Example 2(with 2:5 sequence)
```python
#range(start, stop, step)
#-------------------#
for i in range(5, 2, -1):
    print(i)
#-------------------#
5
4
3#startswith 5, endswith 2+1 = 3(the last one is not used)
```

* Example 3(with a list)
```python
mylist = ['l', 'o', 'o', 'p']
#-------------------#
for i in mylist:
    print(i)
#-------------------#
l
o
o
p#startswith 0, endswith len(mylist) = 4
```

### break

It's same as break of 'while'

### continue

It's same as continue of 'while'

### Multiple for loop statements

```python
for i in iterable1 
    for j in iterable2
     operation
```

* Example 1
```python
mylist = ['l', 'i', 's', 't']
xylist = [1, 2]
#-------------------#
for i in mylist:
    for j in xylist: 
        print(i + str(j))#str() for converting int to str
#-------------------#
l1
l2
i1
i2
s1
s2
t1
t2
#loop len(mylist) * len(xylist) = 4 * 2 = 8 outputs
```

* Example 2(itertools.product( ))
```python
mylist = ['l', 'i', 's', 't']
xylist = [1, 2]
#-------------------#
import itertools
for i, j in itertools.product(mylist, xylist):
    print(i + str(j))#str() for converting int to str
#-------------------#
l1
l2
i1
i2
s1
s2
t1
t2
#loop len(mylist) * len(xylist) = 4 * 2 = 8 outputs
```

### zip( )(Parallel loop)

* Example
```python
mylist = ['l', 'i', 's', 't']
xylist = [1, 2]
#-------------------#
for i, j in zip(mylist, xylist):
    print(i + str(j))#str() for converting int to str
#-------------------#
l1
i2
#zip( ) generates an iterable values(pairing sequences)
list(zip(mylist, xylist))#[('l', 1), ('i', 2)]; its length = the shortest sequence
```

[↑ Up to the Top](#control-flow-statements(conditionals-&-loops))


---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_basic.md#basics-on-python)

