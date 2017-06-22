# Python Multithreading

## ```threading```

You can use ```threading.Thread``` to operate multi-threading jobs.
```run()``` Method is required to use it.

```python
import threading


class messenger(threading.Thread):
    
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

send = messenger(name='Sending...')
receive = messenger(name='Receiving...')
send.start()
receive.start()

Sending...
Sending...
Sending...
Sending...
Sending...
Sending...
Receiving...
Receiving...
Receiving...
Receiving...
Receiving...
Sending...
Sending...
Sending...
Sending...
Receiving...
Receiving...
Receiving...
Receiving...
Receiving...
```

```threading``` can make us use multithreading.


## ```multiprocessing```

```python
import multiprocessing as mp
```


Geometric Brownian Motion Simulator:
```python
import math
import numpy as np


def gbmSimulator( (M, I) ):
    """
    M : Time Step
    I : Path
    """
    
    
    S0 = 100
    r = .05
    sigma = .2
    T = 1.
    
    dt = T / M
    paths = np.zeros((M + 1, I))
    paths[0] = S0
    
    for t in range(1, M + 1):
        paths[t] = paths[t - 1] * np.exp((r - .5 * sigma ** 2) *
                                         dt + 
                                         sigma * math.sqrt(dt) *
                                         np.random.standard_normal(I))
    return paths

paths = gbmSimulator( (5, 2) )

Out[ ]: 
array([[ 100.        ,  100.        ],
       [  99.94976099,   99.14653149],
       [ 106.41670363,  108.37233599],
       [ 113.37268768,  115.41356086],
       [ 119.70794979,  127.24228509],
       [ 119.09420198,  135.71834787]])
```

Multiprocessing with 8 cores:
```python
from time import time
import multiprocessing as mp


I = 10000   # Path count
M = 100     # Time Interval count
t = 100     # Simulation Work count


times = []
for w in range(1, 17):
    t0 = time()
    pool = mp.Pool(processes=w)
    res = pool.map(gbmSimulator, t * [(M, I)])
    times.append(time() - t0)

res

Out[ ]:
[array([[ 100.        ,  100.        ,  100.        , ...,  100.        ,
          100.        ,  100.        ],
        [  95.4614054 ,   99.32541185,   99.29378877, ...,   99.35183236,
          101.62628441,   94.02503549],
        [  97.10811184,   97.59807847,   98.37464388, ...,   94.96544446,
          101.17951869,   94.02642567],
        ..., 
        [ 109.23640209,  117.45733482,   85.59906901, ...,  121.98372504,
           99.81951919,   68.90487463],
        [ 108.51083798,  118.48864251,   86.65450804, ...,  122.57590247,
           99.66786906,   67.16923468],
        [ 109.42731802,  120.51233245,   87.4577772 , ...,

```

## Comparison 1: ```threading``` and ```multiprocessing```

Single Thread:
```python
from threading import Thread
import time

def do_work(start, end, result):
    sum = 0
    for i in range(start,end):
        sum += i
    result.append(sum)
    return

if __name__=='__main__':
    s_time = time.time()
    START, END = 0, 80000000
    result = list()
    th1 = Thread(target=do_work, args=(START, END, result))
    th1.start()
    th1.join()
print ('Result : ',sum(result),'time =',time.time()-s_time)

Result :  3199999960000000 time = 4.102916955947876
```

Multi Thread(4):
```python
from threading import Thread
import time

def do_work(start, end, result):
    sum = 0
    for i in range(start,end):
        sum += i
    result.append(sum)
    return

if __name__=='__main__':
    s_time = time.time()
    START, END = 0, 80000000
    result = list()
    th1 = Thread(target=do_work, args=(START, 20000000, result))
    th2 = Thread(target=do_work, args=(20000000, 40000000, result))
    th3 = Thread(target=do_work, args=(40000000, 60000000, result))
    th4 = Thread(target=do_work, args=(60000000, 80000000, result))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()
print ('Result : ',sum(result),'time =',time.time()-s_time)

Result :  3199999960000000 time = 4.58615517616272
```


Multi Processing:
```python
from multiprocessing import Process, Queue
import time

def do_work(start, end, result):
    sum = 0
    for i in range(start,end):
        sum += i
    result.put(sum)
    return

s_time = time.time()
if __name__=='__main__':
    START, END = 0, 80000000
    result = Queue()
    pr1 = Process(target=do_work, args=(START, int(END/2), result))
    pr2 = Process(target=do_work, args=(int(END/2), END, result))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()
    result.put('STOP')
    sum = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP' : break
        else: sum += tmp
print ('Result : ',sum,'time =',time.time()-s_time)

Result :  3199999960000000 time = 2.290956735610962
```

## Comparison 2: ```threading``` and ```multiprocessing```

```python

from threading import Thread
from queue import Queue
import urllib.request

import json
from urllib.request import urlopen
 
exchange = urlopen("http://api.fixer.io/latest?base=USD").read().decode("utf-8")
ex = json.loads(exchange)

url = 'http://fx.kebhana.com/fxportal/jsp/RS/DEPLOY_EXRATE/fxrate_all.html'


def getRate(pair, outq, url_tmplt=url):
    with urllib.request.urlopen(url_tmplt.format(pair)) as res:
        body = res.read()
        outq.put((pair, float(body.strip())))

getRate('$',)
if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('pairs', type=str, nargs='+')
    args = parser.parse_args()

    outputq = Queue()
    for pair in args.pairs:
        t = Thread(target=getRate, kwargs={'pair': pair,
                                           'outq': outputq})

        t.daemon = True
        t.start()

    for _ in args.pairs:
        pair, rate = outputq.get()
        print(pair, rate)
        outputq.task_done()
    outputq.join()

#%%

import json
from urllib.request import urlopen
 
exchange = urlopen("http://api.fixer.io/latest?base=USD").read().decode("utf-8")
ex = json.loads(exchange)
 
def exCal(dollar):
    exchange = urlopen("http://api.fixer.io/latest?base=USD").read().decode("utf-8")
    ex = json.loads(exchange)
    for rate in sorted(ex.get('rates').keys()) :    
        print(rate+" "+str(dollar*ex.get('rates').get(rate)))
 
exCal(100)
```
