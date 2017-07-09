[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)


---

# Control Flow

* [with Statements](#for-statements)

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


[↑ Up to the Top](#control-flow-statements(conditionals-&-loops))


---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)

