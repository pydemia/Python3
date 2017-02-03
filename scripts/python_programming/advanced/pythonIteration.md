# Iteration in Python

* ```container```
* ```iterable```
* ```iterator```
* ```generator```
* ```coroutine```
* ```asynchronous```

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

## Container

Any object can return one of its items(members).  


```list```
```set```  
```dict```  
```tuple```  
...  


## Iterables



An ```iterable``` can return an ```iterator``` with the purpose of returning __all(!) of its elements__. ( by ```__iter__()``` )  
An Sequencial object can be an ```iterable```. ( by ```__getitem__()``` ) == most containers are also iterable.  
\* ```iter()```: built-in function for making an ```iterator``` object with an ```iterable```
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
It is named ```generator``` since it can literally generate an item with ```yield``` operator, like an factory.  


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

```yield``` operator looks like ```return``` operator, but it plays an input-taker role as well. When Python arrives ```yield``` operator, it generates(not return) an value and standby until ```__next___()``` Method is called, and so on.

#### Generator Comprehension
```python
(expression for expression in itreables)
(expression for expression in itreables if condition)
```

