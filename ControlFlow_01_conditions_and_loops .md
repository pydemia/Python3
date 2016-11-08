[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)


# Control Flow Statements(Conditions & Loops)

* [Conditions](#conditions)
* [if statememts](#if-statements)
* [while statements](#while=statements)
* [for statements](#for-statements)

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

[↑ Up to the Top](#control-flow-statements)

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

[↑ Up to the Top](#control-flow-statements)

---
## While Statements

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
    number = x[ord]
    if x % 2 == 0:#if 'x' is even number
        print('An even number is detected!')
        break
    x += 1
else: 
    print ('There is no even number found!')
#-------------#
"There is no even number found!"
```

[↑ Up to the Top](#control-flow-statements)

---
## for statement

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

### words

### Operation
 
```python
codes
```


[↑ Up to the Top](#control-flow-statements)

---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/README.md)

