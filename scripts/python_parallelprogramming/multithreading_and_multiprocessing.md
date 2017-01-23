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
