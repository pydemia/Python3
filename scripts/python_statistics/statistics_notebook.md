# Statistics

## Basic Statistics


```py
import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats as st
import sklearn as sl

import matplotlib.pyplot as plt

from unipy.sample.datasets import dataManager as dm
dm.init()
dm.datalist()
data = dm.load(dm.datalist()[0])
col = data['age']
```

### Representative Values

```py


# Mean
col.mean()
np.mean(col)
sp.mean(col)
np.nanmean(col)

# Median
col.median()
np.median(col)
sp.median(col)
np.nanmedian(col)

# Max(Min)
max(col)
col.max()
np.max(col)
np.maximum(col, col) # Returns an NDarray with Element-wise Max elements
sp.maximum(col, col) # Returns an NDarray with Element-wise Max elements
np.nanmax(col)  # Returns an NDarray
                # fmax amax maximum

```

### Populations & Samples

* [Scipy : numpy.random](https://docs.scipy.org/doc/numpy/reference/routines.random.html)

### Distributions


* F-Dist.
```py
dfn, dfd = 29, 18
mean, var, skew, kurt = st.f.stats(dfn, dfd, moments='mvsk')

x = np.linspace(st.f.ppf(0.01, dfn, dfd), st.f.ppf(0.99, dfn, dfd), 100)
fig, ax = plt.subplots(1, 1)
ax.plot(x, st.f.pdf(x, dfn, dfd), 'r-', lw=5, alpha=0.6, label='f pdf')

```


### Hypothesis Test



### Population Estimation


#### Point Estimation


#### Interval Estimation


### Analysis of Variance (ANOVA)


### Correlation Analysis


### Regression Analysis


### Time-Series Analysis


#### Auto Regressive Intergrated Moving Average (ARIMA)
