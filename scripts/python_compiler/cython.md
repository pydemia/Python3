# Cython

## `setup.py`

Basic:
```py
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(['aa.pyx', 'bb.pyx'])

```


```py
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("aa", ["aa.pyx"]),
    Extension("bb", ["bb.pyx"]),
    ...
]

setup(
  name = 'MyProject',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
)
```

Run:
```sh

```

## `.pyx` file


## `.html` for profiling

White        : C Call
Light Yellow : C Call > Python Call
Dark Yellow  : C Call < Python Call

```sh
cython -a aa.pyx
```


## Data Types

### Variables:
```py
cdef int i, j, k
cdef float f, g[42], *h
```

### Structs:	
```py
cdef struct Grail:
    int age
    float volume
```
..note Structs can be declared as cdef packed struct, which has the same effect as the C directive #pragma pack(1).

### Unions:	
```py
cdef union Food:
    char *spam
    float *eggs
```

### Enums:	
```py
cdef enum CheeseType:
    cheddar, edam,
    camembert
```

Declaring an enum as cpdef will create a PEP 435-style Python wrapper:

```py
cpdef enum CheeseState:
    hard = 1
    soft = 2
    runny = 3
```

### Functions:	
```py
cdef int eggs(unsigned long l, float f):
    ...
```

#### Parameters
```py
def spam(int i, char *s):
    ...

    cdef int eggs(unsigned long l, float f):
        ...
```


### Extension Types:

```py 	
cdef class Spam:
    ...
```

Note Constants
Constants can be defined by using an anonymous enum:

```py
cdef enum:
    tons_of_spam = 3
```



### Pandas Cython

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 01:23:06 2017

@author: pydemia
"""


import numpy as np
import pandas as pd

df = pd.DataFrame({'a': np.random.randn(1000),
                    'b': np.random.randn(1000),
                    'N': np.random.randint(100, 1000, (1000)),
                    'x': 'x'})

# %%

def f(x):
     return x * (x - 1)
   
def integrate_f(a, b, N):
     s = 0
     dx = (b - a) / N
     for i in range(N):
         s += f(a + i * dx)
     return s * dx
 
# %%

%timeit df.apply(lambda x: integrate_f(x['a'], x['b'], x['N']), axis=1)
%prun -l 4 df.apply(lambda x: integrate_f(x['a'], x['b'], x['N']), axis=1)

# %%
%load_ext Cython


# %%
%%cython
def f_plain(x):
    return x * (x - 1)

def integrate_f_plain(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_plain(a + i * dx)
    return s * dx

# %%
%timeit df.apply(lambda x: integrate_f_plain(x['a'], x['b'], x['N']), axis=1)

# %%

%%cython
cdef double f_typed(double x) except? -2:
    return x * (x - 1)

cpdef double integrate_f_typed(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_typed(a + i * dx)
    return s * dx

# %%
%timeit df.apply(lambda x: integrate_f_typed(x['a'], x['b'], x['N']), axis=1)


# %%

%%cython
cimport numpy as np
import numpy as np
cdef double f_typed(double x) except? -2:
    return x * (x - 1)
cpdef double integrate_f_typed(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_typed(a + i * dx)
    return s * dx

cpdef np.ndarray[double] apply_integrate_f(np.ndarray col_a, np.ndarray col_b, np.ndarray col_N):
    assert (col_a.dtype == np.float and col_b.dtype == np.float and col_N.dtype == np.int)
    cdef Py_ssize_t i, n = len(col_N)
    assert (len(col_a) == len(col_b) == n)
    cdef np.ndarray[double] res = np.empty(n)
    for i in range(len(col_a)):
        res[i] = integrate_f_typed(col_a[i], col_b[i], col_N[i])
    return res

# %%
%timeit apply_integrate_f(df['a'].values, df['b'].values, df['N'].values)
a = [1,2,3]

# %%
cpdef f_test(a, b, scale=1, alternative='two-sided', conf_level=.95, *args, **kwargs):
    
    assert 0 < scale <= 1
    assert 0 < conf_level <= 1

    dfn = len(a) - 1
    dfd = len(b) - 1

    if (len(a) or len(b)) < 2:

        print('Observations are insufficient.')
        f_statistics = np.nan
        p_value = np.nan
        conf_min, conf_max = np.nan, np.nan

    else:

        var_a = pd.Series(a).var()
        var_b = pd.Series(b).var()

        try:
            f_statistics = var_a / var_b
        except ZeroDivisionError:
            f_statistics = np.nan
 
        p_value = st.f.cdf(np.abs(f_statistics), dfn, dfd, scale=scale)
        #p_value = distributions.t.sf(np.abs(t), df)

        conf_interval = st.f.interval(conf_level, dfn, dfd, scale=scale)
        conf_min, conf_max = np.multiply(f_statistics, conf_interval)


        if alternative == 'two-sided':
            p_value = 2 * np.min([p_value, 1-p_value])

        elif alternative == 'greater':
            p_value = st.f.sf(f_statistics, dfn, dfd, scale=scale)
            conf_min, conf_max = conf_min, np.inf

        elif alternative == 'less':
            conf_min, conf_max = 0, conf_max


    #print('F-Statistics: %.4g' % f_statistics)
    #print('dfn, dfd: %d %d' % (dfn, dfd) )
    #print('Hypothesized Scale: %d' % scale)
    #print('Confidence Level: %.3g' % conf_level)
    #print('Confidence Interval: %.4g, %.4g' % (conf_min, conf_max))
    #print('P-value: %.4g' % p_value)

    res = pd.Series( {'f_statistics': f_statistics,
                      'dfn': dfn,
                      'dfd': dfd,
                      'hypo_scale': scale,
                      'conf_level': conf_level,
                      'conf_interval': (conf_min, conf_max),
                      'p_value': p_value} )

    return res

# %%

%%cython
cimport cython
cimport numpy as np
import numpy as np
cdef double f_typed(double x) except? -2:
    return x * (x - 1)
cpdef double integrate_f_typed(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_typed(a + i * dx)
    return s * dx

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[double] apply_integrate_f_wrap(np.ndarray[double] col_a, np.ndarray[double] col_b, np.ndarray[int] col_N):
    cdef int i, n = len(col_N)
    assert len(col_a) == len(col_b) == n
    cdef np.ndarray[double] res = np.empty(n)
    for i in range(n):
        res[i] = integrate_f_typed(col_a[i], col_b[i], col_N[i])
    return res



# %%
df.eval("""
c = a + b
d = a + b + c
a = 1""", inplace=False)
```

