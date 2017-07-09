[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_advanced.md#advanced-python)



# Coroutine
Coroutine: kind of Improved Generator.
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

```yield from``` is important for open channels between the outbound ```callers``` and the inner ```generators```

## Coroutine

* Body 안에 yield 문을 가진 일종의 Generator
* 값을 반환할 수 있는 Generator
* yield from 구문을 이용해서 하위 Generator로 re-factoring할 수 있게 한다,

---
### 기본 동작 

```python
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

my_cor = simple_coroutine()
my_coro
next(my_coro)
my_coro.send(42)
```

### Coroutine의 기본 상태
* **'GEN_CREATED'**: 실행 전 대기 상태  
* **'GEN_RUNNING'**: 실행 중(by Interpreter)  
* **'GEN_SUSPENDED'**: yield 문에서 대기하는 상태
* **'GEN_CLOSED'**: 실행완료 상태

### Example: Moving Average Coroutine

```python
def averager():
    total = 0.0
    count = 0
    averate = None
    while True:
          term = yield average
          total += term
          count += 1
          average = total/count
coro_avg = averager()
next(coro_avg)#None
coro_avg.send(10)#10.0
coro_avg.send(30)#20.0
coro_avg.send(5)#15.0
```

### @coroutine: Coroutine을 기동하기 위한 Decorator
```python
from functools import wraps

def coroutine(func):
    """데커레이터: 'func'를 기동해서 첫 번째 'yield'까지 진행한다."""
    @wraps(func)
    def primer(*args, **kwargs): #decorate된 Generator 함수는 primer 함수로 치환, 실행 시 기동된 Generator 반환
        gen = func(*args, **kwargs) #decorate된 함수를 호출, Generator 객체 가져오기
        next(gen) #Generator 기동
        return gen #Generator 반환
    return primer
```

---
### Example: Moving Average with Decorator(@coroutine)
```python
coro_avg = averager()
from inspect import getgeneratorstate
getgeneratorstate(coro_avg)#'GET SUSPENDED': ready to receive a value

from coroutil import coroutine

@coroutine
def averager():
    totoal = 0.0
    count = 0
    average = None
    while True:
          term = yield average
          total += term
          count += 1
          average = total/count
```

---
### Coroutine 종료, 예외 처리: throw(), close() Method

* **generator.throw(exc_type[, exc_value[, trackback]])**  
> Generator가 중단한 곳의 yield 표현식에 예외 전달  
> Generator가 예외를 처리하면, 다음 yield 문까지 진행하고 생성값은 generator.throw() 호출 값이 됨.  
> 예외 처리를 하지 않으면 Caller까지 예외 전파

* **generator.close()**
> Generator가 실행을 중단한 yield 표현식이 GeneratorExit 예외를 발생하게 함.  
> Generator가 예외 처리를 하지 않거나 StopIteration 예외(일반적으로, Generator 실행 완료 시 발생)를 발생시키면,  
> 아무 에러도 Caller에 전달되지 않음.  
> Generator는 GeneratorExit 예외를 받으면 아무 값도 생성하지 않아야 함, 아니면 RuntimeError 예외 발생

#### Example
```python
class DemoException(Exception):

def demo_exc_handling():
    print('-> coroutine started')
    while True:
          try:
              x = yield
          except DemoException:
                 print('*** DemoException handled. Continuing...')
          else:
                 print('-> coroutine received: {!r}'. format(x))
    raise RuntimeError('THis line sould never run.')

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.close()
from inspect import getgeneratorstate
getgeneratorstate(exc_coro)#'GET_CLOSED'
```
이 무한루프는 처리되지 않은 예외에 의해서만 중단, 예외 처리하지 않으면 Coroutine 실행이 중단됨.
---


[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_advanced.md#advanced-python)
