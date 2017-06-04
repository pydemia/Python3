[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)


# Objects

---
## Comprehensions

The Compact ways to generate Data Structures using Iterators.


### List Comprehension

```python
[expression for items in iterables]
[expression for items in iterables if condition]
```

* Example
```python
mylist = [i for i in range(2,8)]
mylist#[2, 3, 4, 5, 6, 7]

mylist = [i+1 for i in range(2,8)]
mylist#[3, 4, 5, 6, 7, 8]

mylist = [i for i in range(2, 8) if i % 2 != 0]
mylist#[3,5,7]

mylist = ['a', 'b', 'c']
xylist = [1, 2]
ids = [(i, j) for i in mylist for j in xylist]#generate a list of tuples
for i, j in ids:#Unpacking a tuple!
    print(i, j)
```

### Dictionary Comprehension

```python
{ key_exp : val_exp for expression in iterables}
{ key_exp : val_exp for expression in iterables if condition}
```

* Example

```python
{i : i**2 for i in range(1,6)}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

{i : i**2 for i in range(1,6) if i < 4}
{1: 1, 2: 4, 3: 9}
```


### Set Comprehension

```python
{expression for expression in itreables}
{expression for expression in itreables if condition}
```

* Example

```python
words = "python"
{i for i in words if i != "p"}
{'t', 'o', 'h', 'n', 'y'}
```

### Generator Comprehensions(NOT TUPLE COMPREHENSIONS!)

```python
(expression for expression in itreables)
(expression for expression in itreables if condition)
```

This returns a Generator object.[Go to "Generators"](https://github.com/pydemia/Python3/blob/master/scripts/python_programming/advanced/pythonIteration.md#generator)

[↑ Up to the Top](#control-flow-statements(conditionals-&-loops))

[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)
