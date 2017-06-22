# Python Asynchronous I/O, event loops, ...


To understand ```asyncio```, You need to know ```generator``` and ```coroutine``` first.

* [Generators](https://github.com/pydemia/Python3/blob/master/scripts/python_programming/Functions_01_basics.md#generators)
* [Coroutines](https://github.com/pydemia/Python3/blob/master/scripts/python_programming/ControlFlow_03_coroutine.md#coroutine)


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


### Example: Coroutine displaying the current date
```python
import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
#loop.close()
```

With ```generator```:

```python
@asyncio.coroutine
def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(1)
```

### Example: Parallel execution of tasks

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
#loop.close()
```
