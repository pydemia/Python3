# Statistics

## Basic Statistics


```py
import numpy as np
import pandas as pd
import scipy as sp
import sklearn as sl

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
np.nanmax(col)  # Returns an NDarray with 
                # fmax amax maximum

```

### Populations & Samples


### Distributions


### Hypothesis Test


### Population Estimation


#### Point Estimation


#### Interval Estimation


### Analysis of Variance (ANOVA)


### Correlation Analysis


### Regression Analysis


### Time-Series Analysis


#### Auto Regressive Intergrated Moving Average (ARIMA)
