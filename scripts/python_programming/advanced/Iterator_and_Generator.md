[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_advanced.md#advanced-python)


# Iterables, Iterator, Generator
데이터 처리를 위한 반복작업을 위한 항목

---
##Iterables(반복형): 

iter() 내장함수가 Iterator를 가져올 수 있는 모든 객체,  
호출될 때마다 Iterator를 새로 생성, 반환하는 \_\_iter\_\_() Method를 구현하는 객체  
/Sequence도 포함;0에서 시작하는 Index를 받는 \_\_getitem\_\_() Method를 구현하는 객체

---
##Iterator(반복자)

self를 반환하는 \_\_iter\_\_() Method를 구현하고,  
다음 항목을 개별로 반환하거나, 다음 항목이 없을 때 StopIteration 예외를 발생시키는,  
인수를 받지 않는 \_\_next\_\_() Method를 구현하는 객체.


####Iterator Pattern을 사용해야 할 때

* 집합 객체의 내부 표현을 노출시키지 않고 내용에 접근하는 경우
* 집합 객체의 다중 반복을 지원하는 경우
  (동일한 Iterable Object로부터 Multiple Independent Iterators를 가질 수 있어야 하며,  
   이때 각 Iterator는 고유한 내부 상태를 유지해야 함.: iter(myiterable)호출할 때마다 독립 Iterator가 새로 생성)
* 다양한 집합 구조체를 반복하기 위한 통일된 Interface를 제공하는 경우


Iterator는 Iterables이기도 함.(\_\_iter\_\_() Method도 구현하므로)  
Iterables는 Iterator가 아님.(\_\_next\_\_() Method가 없으므로)

---
###Iterables에 대한 Regular Interface
####\_\_iter\_\_()
self 반환;for loop 등 Iterables가 필요한 곳에 Iterator 사용 가능하게 함.


###Iterator에 대한 Regular Interface
####\_\_next\_\_()
다음 항목 반환, 없으면 StopIteration 발생
```python
def __next__(self):
    raise StopIteration
```
####\_\_iter\_\_()
self 반환;for loop 등 Iterables가 필요한 곳에 Iterator 사용 가능하게 함.
```python
def __iter__(self):
    return self
```

---
##Generator: yield Operator
내부에 yield 키워드를 가진 함수,  
(Generator는 yield에 전달된 표현식의 값을 생성하는 Iterator)  
Generator Function은 Genarator Object를 반환.


모든 Generator는 Iterator, but  
Iterator는 Collection에서 항목을 가져오지만,  
Generator는 항목을 생성할 수 있음(Collection을 미리 만들어 둘 필요 없음).  
지능형 리스트의 Lazy Version.

### Generator Example
```python
def __iter__(self):
    for word in self.words:
        yield word
    return iter(self.words)
def gen():
    for i in range(10):
        yield i ** 3
for x in gen():
    print(x)
```
---
###yield Operator
return과는 다르게 함수 중간에 빠져나와 값을 반환,  
Generator는 yield에 전달된 표현식의 값을 생성하는 Iterator.
> next()의 Caller(호출자)에 반환될 값을 생성/양보하여 Caller가 작업 진행,  
> 이후 Caller가 다른 값을 필요로 하여 다음 번 next()를 호출할 때 까지  
> Generator 실행을 중단

###yiled from
다른 Generator에서 생성된 값을 상위 Generator 함수가 생성해야 할 때

####기존: for loop
```python
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
```

####yield from
```python
def chain(*iterables):
    for it in iterables:
        yield from i
```

---
###Lazy Evaluation
메모리 한계를 극복하기 위해 한 번에 한 항목씩 순차적으로 데이터를 처리하는 계산 방법 

#### Generator Example:Arithmetic Progression Class
```python
class ArithmeticProgression:

   def __init__(self, begin, step, end=None):
       self.begin = begin
       self.step = step
       self.end = end #None: Infinite

   def __iter__(self):
       result = type(self.begin + self.step)(self.begin)
       forever = self.end is None
       index = 0
       while forever or result < self.end:
             yield result
             index += 1
             result = self.begin + self.step * index
```

---
### 표준 Library의 Generator Function
```python
from itertools import *
from functools import *
```


[← back to *Main Page*](https://github.com/pydemia/Python3/blob/master/scripts/PythonProgramming_advanced.md#advanced-python)
