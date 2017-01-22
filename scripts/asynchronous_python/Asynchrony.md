# Python Asynchronous I/O, event loops, ...


To understand ```asyncio```, You need to know ```generator``` and ```coroutine``` first.

## Generator

It is a Function generates an Iterator.
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

## Coroutine

```generator``` is used by generating & getting values. ```coroutine``` is used by pushing a value with ```.send()``` Method.

```python
from inspect import getgeneratorstate as gs

def coroutineObject(number):
    
    print('Started: a:', number)
    res1 = yield number
    
    print('Received: b:', number)
    print('Calculation: a + b')
    res2 = yield res1 + number
    
    print('Received: c:', number)
    res3 = yield res2 * number
    
    print('Cannot Receive {}. It\'s over'.format(number))

```

```python
myco = coroutineObject(3)

# 'GEN_CREATED' ----------#
myco
Out[]: <generator object coroutineObject at 0x7f282906c360>

gs(myco)
Out[]: 'GEN_CREATED'


# 'GEN_SUSPENDED' 1 ------#
next(myco)
Started: a: 3
Out[]: 3

gs(myco)
Out[]: 'GEN_SUSPENDED'

# 'GEN_SUSPENDED' 2 ------#
myco.send(5)
Received: b: 5
Calculation: a + b
Out[]: 8

gs(myco)
Out[]: 'GEN_SUSPENDED'

# 'GEN_SUSPENDED' 3 ------#
myco.send(10)
Received: b: 5
Calculation: a + b
Out[]: 8

gs(myco)
Out[]: 'GEN_SUSPENDED'

# 'GEN_CLOSED' -----------#
myco.send(7)

Cannot Receive 3; It's over
Traceback (most recent call last):

  File "<ipython-input-154-ddb1255cc7ad>", line 1, in <module>
    myco.send(7)

StopIteration

gs(myco)
Out[]: 'GEN_CLOSED'
```

```coroutine``` uses ```yield``` Statement not to return a result but to receive a input. Since it operates like a ```generator```, the assignment cannot generate a value;```GEN_CREATED```. We called ```next()``` Method to initiate it. It stops after the first ```yield``` Statement.  
It can receive inputs with ```send()``` Method. Each operation stops and awaits a input after the ```yield``` Statements;```'GEN_SUSPENDED'```. ```coroutine``` runs & stops the iteration if all ```yield``` Statements are used. ```myco.send(7)``` operates the remaining but cannot receive ```7``` since there are no ```yield``` Statement anymore. That's why it was printed ```Cannot Receive 3. It's over```, not```Cannot Receive 7```. and then it ends with showing ```StopIteration``` Exception.  


### Advanced Coroutine

Use ```yield```:

```python
def gen():
    
    for c in 'AB':
        yield c
    
    for i in range(1, 3):
        yield i
```

```python
list(gen())
Out[]: ['A', 'B', 1, 2]
```

Use ```yield from```:

```python
def gen():
    yield from 'AB'
    yield from range(1,3)
```

```python
list(gen())
Out[]: ['A', 'B', 1, 2]
```

```yieldfrom``` is important for open channels between the outbound ```callers``` and the inner ```generators```


## Asyncio


A normal Function:

```python
import timeit
from urllib.request import urlopen

urls = ['http://b.ssut.me', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']
start = timeit.default_timer()

for url in urls:
    print('Start', url)
    urlopen(url)
    print('Done', url)

duration = timeit.default_timer() - start 

# Start http://b.ssut.me
# Done http://b.ssut.me
# Start https://google.com
# Done https://google.com
# Start https://apple.com
# Done https://apple.com
# Start https://ubit.info
# Done https://ubit.info
# Start https://github.com/ssut
# Done https://github.com/ssut
# => duration = 2.4946455230019637
```


Using ```thread```

```python
import timeit
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

urls = ['http://b.ssut.me', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']

def fetch(url):
    print('Start', url)
    urlopen(url)
    print('Done', url)

start = timeit.default_timer()
with ThreadPoolExecutor(max_workers=5) as executor:
    for url in urls:
        executor.submit(fetch, url)

duration = timeit.default_timer() - start

# Start http://b.ssut.me
# Start https://google.com
# Start https://apple.com
# Start https://ubit.info
# Start https://github.com/ssut
# Done https://ubit.info
# Done http://b.ssut.me
# Done https://google.com
# Done https://apple.com
# Done https://github.com/ssut
```

Using ```asyncio```, ```aiohttp```
```python

import aiohttp
import asyncio
import timeit

@asyncio.coroutine
def fetch(url):
    print('Start', url)
    req = yield from aiohttp.request('GET', url)
    print('Done', url)

@asyncio.coroutine
def fetch_all(urls):
    fetches = [asyncio.Task(fetch(url)) for url in urls]
    yield from asyncio.gather(*fetches)

urls = ['http://b.ssut.me', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']

start = timeit.default_timer()
asyncio.get_event_loop().run_until_complete(fetch_all(urls))
duration = timeit.default_timer() - start

# Start http://b.ssut.me
# Start https://google.com
# Start https://apple.com
# Start https://ubit.info
# Start https://github.com/ssut
# Done https://ubit.info
# Done http://b.ssut.me
# Done https://google.com
# Done https://apple.com
# Done https://github.com/ssut
# => duration = 0.9832467940016068
```
