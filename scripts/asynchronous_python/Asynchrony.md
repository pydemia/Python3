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


## Sequential Crawler

```python

import grequests
import string
import random


def generate_urls(base_url, num_urls):
    for i in xrange(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))


def run_experiment(base_url, num_iter=500):
    urls = generate_urls(base_url, num_iter)
    requests = (grequests.get(u) for u in urls)
    response_futures = grequests.imap(requests, size=100)
    response_size = sum(len(r.text) for r in response_futures)
    return response_size

if __name__ == "__main__":
    import time
    delay = 100
    num_iter = 500

    start = time.time()
    result = run_experiment(
        "http://127.0.0.1:8080/add?name=grequests&delay={}&".format(delay),
        num_iter)
    end = time.time()
    print result, (end - start)
```


## 
