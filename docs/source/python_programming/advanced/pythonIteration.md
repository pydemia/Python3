# Iteration in Python

* [```container```](#containers)
* [```iterable```](#iterables)
* [```iterator```](#iterators)
* [```generator```](#generators)
* [```coroutine```](#coroutine)
* [```asynchronous```]()

## subroutine & coroutine

---
#### Comparision

```python

def func():            # a generic function
    return

def genfunc():         # a generator function
    yield

async def coro():      # a coroutine function
    await smth()

async def asyncgen():  # an asynchronous generator function
    await smth()
    yield 42

```

---

## Containers

Any object can return one of its items(members).  


* ```list```
* ```set```  
* ```dict```  
* ```tuple```  
...  


## Iterables

An ```iterable``` can return an ```iterator``` with the purpose of returning __all(!) of its elements__. ( by ```__iter__()``` )  
An Sequencial object can be an ```iterable```. ( by ```__getitem__()``` ) == most containers are also iterable.  
\* ```iter()```: built-in function for making an ```iterator``` object with an ```iterable```.  
All ```iterable```s returns an ```iterator``` with ```iter()```:  


```python
# list_iterator
mylist = [1, 2, 3, 4, 5]
iter(mylist)

Out[]:
<list_iterator at 0x7f44e6b7b860>


# set_iterator
myset = set(mylist)
for _ in myset:
    print(_)

Out[]:
<set_iterator at 0x7f44ded0daf8>


mylist = [1, 2, 3, 4, 5]
iter(mylist)

Out[]:
<list_iterator at 0x7f44e6b7b860>


# dict_key_iterator
mydict = {'a': 1, 'b': 2, 'c': 3}
iter(mydict)

Out[]:
<dict_keyiterator at 0x7f44bc0d0d18>

```



## Iterators
Any object can produce(return) the next item when you call ```next()``` on it.
```iterator``` can return its item(member) next to next, one by one. If finished, it raises ```StopIteration``` Exception( by ```__next__()``` )  
\* ```next()```: built-in function for returning the next item in an ```iterator```

```python
mylist = [1, 2, 3]
myiter = iter(mylist)
next(myiter)  # 1
next(myiter)  # 2
next(myiter)  # 3
next(myiter)  # StopIteration exception
```

```itertools.count``` is an ```iterator```, which produces the next value unlimitedly.  

An example:
```python
import itertools as it
counter = it.count(start=3)
next(counter)  # 3
next(counter)  # 4
next(counter)  # 5

```

Tip: You can make an infinite ```iterator``` with an finite ```iterable```

```python
import itertools as it

mylist = [1, 2, 3]
number = it.cycle(mylist)
next(number)  # 1
next(number)  # 2
next(number)  # 3
next(number)  # 1
next(number)  # 2

```

```for``` loop under the hood:
When Python executes the ```for``` loop with a ```container```,
It invokes the ```__iter__()``` Method of the ```container``` to get an ```iterator``` internally. 
And then it repeatedly calls ```__next__()``` Method of the ```iterator``` until ```StopIteration``` exception is raised.



## Generator

An ```iterator``` contains ```yield``` operator, which produces values in lazy.  
It is named ```generator``` since it can literally generate an item with ```yield``` statement, like an factory.  

### ```yield``` Statement

Here is an example:
```python
import itertools as it

def fibonacci():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

fibo = fibonacci()
list(it.islice(fibo, 0, 13))

Out[]:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

next(fibo)  # 377
next(fibo)  # 610

```

```yield``` operator looks like ```return``` statement, but it plays an input-taker role as well.  
When Python arrives ```yield``` statement, it generates(not return) an value and standby until ```__next___()``` Method is called, and so on.


### ```yield from``` Statement

It is used for generator delegation (Subgenerator), allowing a ```generator``` to delegate part of its operations to another ```generator```. You can understand '```yield from``` == ```yield``` a value, with another value from ```yield``` of another ```generator```'.  

This allows a section of code containing ```yield``` to be factored out and placed in another ```generator```. Additionally, the ```subgenerator``` is allowed to return with a value, and the value is made available to the delegating ```generator```. 

For simple iterators, ```yield from iterable``` is essentially just a shortened form of ```for item in iterable: yield item:```


```python
def g(x):
    yield from range(x, 0, -1)
    yield from range(x)

list(g(5))

Out[]:
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
```

Unlike an ordinary loop, yield from allows subgenerators to receive sent and thrown values directly from the calling scope, and return a final value to the outer generator:
```python

def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next

def gather_tallies(tallies):
    while 1:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []
acc = gather_tallies(tallies)
next(acc)  # Ensure the accumulator is ready to accept values


for i in range(4):
    acc.send(i)

acc.send(None)  # Finish the first tally


for i in range(5):
    acc.send(i)

acc.send(None)  # Finish the second tally
tallies

Out[]:
[6, 10]

```

### Generator Comprehension (Generator Expression)
```python
(expression for expression in itreables)
(expression for expression in itreables if condition)
```

### Benefits of using Generator

Memory Usage
```py
import sys
print(sys.getsizeof( [i for i in range(100) if i % 2] ))  # 528
print(sys.getsizeof( [i for i in range(1000) if i % 2] ))  # 4272

print(sys.getsizeof( (i for i in range(100) if i % 2) ))  # 88
print(sys.getsizeof( (i for i in range(1000) if i % 2) ))  # 88

```

Lazy-Evaluation
```py
def operation_checker(x):
    print('Operating...')
    return x

# List
cont = [operation_checker(i) for i in range(10) if i % 2]
for _ in cont:
    print(_)

# Generator
cont = (operation_checker(i) for i in range(10) if i % 2)    
for _ in cont:
    print(_)
```

## Coroutine  


```coroutine``` is similar to ```generator```, but it is the difference that ```generator``` is a value producer and ```coroutine```  is a value consumer. ```yield```Statement in ```coroutine``` receives a value from outside of the Function by ```send()``` Method.  
In Python systax, You can simply understand a ```coroutine``` is made if ```yield``` are assigned as a variable.


#### ```coroutine``` Status

```python
from inspect import getgeneratorstate as gs

gs(coroutine)

```

| Status | Description |
| :----- | :---------- |
| __'GEN_CREATED'__  | Waiting for execution |
| __'GEN_RUNNING'__  | Being executed (by Interpreter) |
| __'GEN_SUSPENDED'__| Being suspended at ```yield``` Statement after generating a value |
| __'GEN_CLOSED'__   | execution ended |


### Native ```coroutine``` from ```generator```


a ```generator```: a value producer

```python
def fibonacci():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

fibo = fibonacci()
fibo.__next__()  # 1  : (1)    # started
fibo.send(3)     # 1  : (0+1)  # same as next() : because generator cannot receive 3 as a value.
next(fibo)       # 2  : (1+1)  # same as next()
next(fibo)       # 3  : (1+2)
next(fibo)       # 5  : (2+3)
next(fibo)       # 8  : (3+5)
next(fibo)       # 13 : (5+8)

```

a ```coroutine``` : a value consumer

```python
def fibonacciCoro():
    prev, curr = 0, 1
    while True:
        curr += yield
        prev, curr = curr, prev + curr

fiboCoro = fibonacciCoro()
fiboCoro.__next__()  # Noting is shown
fiboCoro.send(3)     # Noting is shown
fiboCoro.send(3)     # Noting is shown
fiboCoro.send(3)     # Noting is shown

```

We have used ```send()``` Method but nothing is shown, unlike the ```generator``` case. Actually It worked! The only problem is that ```yield``` Statements in ```coroutine``` only receive a given value by ```send()``` Method, don't produce something.  
If you want to check it, put ```print()``` function in the Function:

```python
def fibonacciCoro():
    prev, curr = 0, 1
    while True:
        curr += yield
        print(curr)
        prev, curr = curr, prev + curr

fiboCoro = fibonacciCoro()
fiboCoro.__next__()  # Nothing is shown : (1)  # started
fiboCoro.send(3)     # 4  : (1) + 3
fiboCoro.send(3)     # 7  : (0+4) + 3
fiboCoro.send(3)     # 14 : (4+7) + 3
fiboCoro.send(3)     # 24 : (7+14) + 3
fiboCoro.send(3)     # 41 : (14+24) + 3

```

To understand the roles of ```yield``` Statements in separate, put it together in the Function:

```python
def fibonacciCoro():
    prev, curr = 0, 1
    while True:
        curr += yield
        yield curr
        prev, curr = curr, prev + curr

fiboCoro = fibonacciCoro()
fiboCoro.__next__()  # Nothing is shown : (1)  # started
fiboCoro.send(3)     # 4  : (1) + 3     : suspended at 2nd yield, yield as a producer
fiboCoro.send(3)     # Nothing is shown : yield as a consumer
fiboCoro.send(3)     # 7  : (0+4) + 3   : suspended at 2nd yield, yield as a producer
fiboCoro.send(3)     # Nothin is shown  : yield as a consumer
fiboCoro.send(3)     # 14 : (4+7) + 3   : suspended at 2nd yield, yield as a producer

```

### Asynchronous Coroutines

### ```@asyncio.coroutine``` with ```yield from``` Statements

```python

```

### ```coroutine``` with ```async``` / ```await``` : For ```asyncio``` API only

```python

``

