# Control Flow
## Coroutine
Coroutine: kind of Improved Generator

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
* 'GEN_CREATED': 실행 전 대기 상태  
* 'GEN_RUNNING': 실행 중(by Interpreter)  
* 'GEN_SUSPENDED': yield 문에서 대기하는 상태
* 'GEN_CLOSED': 실행완료 상태

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
