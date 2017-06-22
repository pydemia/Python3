[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)

---
# Functions


## Functions as _Objects_

**_Functions_** can be **_Arguments_**.

```python
def adder(a, b):
    return a + b

def runfunc_and_double(func, a, b):
    res = func(a, b)
    return res * 2

runfunc_and_double(adder, 3, 5)
16 # res = adder(3, 5) = 3+5, and res*2 = 8*2 = 16
```




---
## Nested Functions - Inner Functions

You can define a **_Function_** within another **_Function_**.  
It is built for complex operations repeated within Functions.
The inner Functions can access to the variables within the outer functions.  

* The Outer functions have the nested Functions.  
* The Nested Functions(the child functions) refer to the variables of the Outer Function(the parent functions).  
* The Outer Functions(the outer functions) return the Nested Functions(the child functions).  

```python
def runfunc_and_mult(a, b, c):
    def adder(a, b):
        return a + b
    return adder(a, b) * c

runfunc_and_mult(3, 5, 4)
32 # 3+5 = 8, and 8*4 = 32
```




---
## Closures

Closures can be generated to other Functions, and operate & change the variables from _the outer Functions._
When do you use **_Closure_**?  

* Not to use something as a _Global Variables_ but a _Local Variables_.
* Trying to keep & hide the inner data but only to use it.  

You can generate a function from another function with Closure.  
We can preserve given parameters with this.

__Nested Function__
```py
def print_messege(string):

    def printer():
        print(string)

    printer()
```

```py
print_messege('Python')
```

__Closure__
```py
def print_messege(string):

    def printer():
        print(string)

    return printer  # The nested function returns a function itself!
```

```py
print_messege('Python')
Out[ ]: <function __main__.print_messege.<locals>.printer>

closureFunc = print_messege('Python')
closureFunc()

# Python  # The closureFunc is a function that keeps a value from print_messege() was called.
```

This `closureFunc` is preserved even `print_messege` is removed from the namespace.
```py
del print_messege
print_messege()

NameError: name 'print_messege' is not defined
```


```py
closureFunc()

# Python
```

Another example:

```python
def runfunc_and_mult(a, b):
    def adder():
        return a + b
    return adder            # the outer function did not CALL function, but RETURN the copied one.

a = runfunc_and_mult(1,2)
a
<function runfunc_and_mult.<locals>.adder at 0x7fc9bace8620>

type(a)
<class 'function'>

a()
3                          # It remembers the variables from the outer functions.
```





---
## Lambda Functions

Anonymous Functions of Python.  It generates & returns retults **_ONCE_**.  
It is the simple way to generate Functions. You can use **_Lambda Functions_** _temporarily_.  


```lambda``` takes one argument.
```python
[lambda arg: operation(arg)]
```

* Example
```python
numlist = [1, 2, 3, 4]

def editor(numbers, func):
    for i in numbers:
        print(func(i))

def plusone(num):
    return num + 1

editor(numlist, plusone)
2
3
4
5 
```

```lambda``` is more simple!

```python
numlist = [1, 2, 3, 4]

def editor(numbers, func):
    for i in numbers:
        print(func(i))

editor(numlist, lambda i: i+1)
2
3
4
5
```




---
## Generators

The Python Sequence Objects which is a Function generates an Iterator.
It's _iterable_ so you can iterate through HUGE Sequences without creating & storing the entire sequence in memory at once. 



```python
# Create a custom range function
def rangeGenerator(number):
    n = 0
    while n < number:
        yield n
        n += 1
```

```python
rangeGenerator(5)
Out[]: <generator object rangeGenerator at 0x7f2829dd37d8>

tmp = rangeGenerator(5)

next(tmp)
Out[]: 0

next(tmp)
Out[]: 1

next(tmp)
Out[]: 2

next(tmp)
Out[]: 3
next(tmp)
Out[]: 4

next(tmp)
Traceback (most recent call last):

  File "<ipython-input-40-6bbd56cbcde7>", line 1, in <module>
    next(tmp)

StopIteration

```


Usage:
```python
for _ in rangeGenerator(5):
    print (_)
    
Out[]: 
0
1
2
3
4
```
  
A normal function has ```return``` and It is operated only one time. Besides, ```generator``` has ```yield``` instead of ```return```. It returns a result on and on, not repeats the result but operates to the next. It could be done because after ```yield``` returns a result, ```yield``` remembers the operation & the result to operate the next job.  
A ```generator``` returns a ```generator``` object. internally it is called by ```next()``` Method. When we call ```generator``` with ```next()```, ```generator``` operates and stops at the point of ```yield``` Statement.
We generally use ```generator``` in ```for loop``` for extract the results.
Its ADVANTAGE is the less-memory usage for iteration. Creating a list like ```[0,1,2,3,4]``` needs a fixed memory size related to its length. But using a ```generator``` as the above, we need less to keep the status of ```n```.


```generator``` can be used for ```pipeline```

> input --> generator -> generator -> generator -> for x in s:



```range()``` is the most famous generator in Python3(```xrange()``` in Python2).  

Look at the custom ver. of ```range()```
```python
def myrange(start, end, step):
    i = start
    while i < end:
        yield i
        i += step
```

It`s a normal Function,  
and it returns a **_Generator Object_**.  
This function can show how **_Generator_** works.  
```yield``` Statements can throw out the output of ```i```, step by step, while the function is operating(the ```while``` Statement is looping). 

#### Example
In many times, you don't need to generate a list to append elements but each elements itself unless you need a container either. Let's change it;

From:
```python
def returnList():
    res = []
    for _ in iterable:
        res.append(_)
   	return res
```
To:
```python
def generatorExample():
    for _ in iterable:
        yield _
```

---
## Decorators

Using **_Decorators_**, you can modify existing functions without changing it.  
It`s a _Function_ takes one function as input & returns another.

Let`s define a **_Decorator_**.
```python
def plusone(func):
    def function(*args):
        res = func(*args):
        print('res + 1:', res+1)
        return res+1
    return function
```

And then,  define a _normal Function_ and use the**_Decorator_**.

* Case 1: without the Decorator
```python
def adder(a, b):
    return a+b

adder(1, 2)
3 # it returns 3
```

* Case 2: with the Decorator
```python
@plusone
def adder(a, b):
    return a+b

adder(1, 2)
res+1: 4 # print & +1 function: adder function was Decorated!
4         # return the Decoratsed result!
```


You can use multiple **_Decorators_**.  
The closer one decorates the function first.
```python
# Create another Decorator
def double(func):
    def function(*args):
        res = func(*args)
        print('res*2:', res*2)
        return res*2
    return function

@double
@plusone
def adder(a, b):
    return a+b

adder(1, 2)
res+1: 4 # 1. plusone Decorator
res*2: 8 # 2. double  Decorator
```

```python
@print_form
@double
def adder(a, b):
    return a+b

adder(1, 2)
res*2: 6 # 1. double  Decorator
res+1: 7 # 2. plusone Decorator
```



---
[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_intermediate.md#intermediate-python)


