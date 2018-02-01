# Far More Interesting in Python

## Code Pattern

### Lazy Evaluation

#### Lazy Evaluation in Class


* __Eager Evaluation__: execute when it is defined
```py
class Calc:
    def __init__(self, n):
        self.n = n
        self.solution = self._calculate()
    
    def _calculate(self):
        res = ...
        return res
```


* __Eager Evaluation__: execute when it is called

```py
class Calc:
    def __init__(self, n):
        self.n = n
        self.solution = []
    
    @property
    def result(self):
        if not self.result:
            res = self._calculate()
        else:
            res = self.solution
        return res

    def _calculate(self):
        res = ...
        return res
```


### Memoization

#### 5 Ways to write a fibonacci sequence

```py
## Example 1: Using looping technique
def fib(n):
 a, b = 0, 1
 for i in range(n-1):
  a, b = b, a+b
 return a
print fib(5)
 
## Example 2: Using recursion
def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
print fibR(5)
 
## Example 3: Using generators
a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
f.next()
f.next()
f.next()
f.next()
print f.next()
 
## Example 4: Using memoization
def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
  return memo[arg]
 
## fib() as written in example 1.
fibm = memoize(fib,5)
print fibm
 
## Example 5: Using memoization as decorator
class Memoize:
 def __init__(self, fn):
  self.fn = fn
  self.memo = {}
 def __call__(self, arg):
  if arg not in self.memo:
   self.memo[arg] = self.fn(arg)
   return self.memo[arg]
 
@Memoize
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(5)
```
