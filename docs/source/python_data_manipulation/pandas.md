[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonDataManipulation.md)


# Pandas

* ```Series```  
* ```DataFrame```  

## Installation
```sh
pip install pandas
conda install pandas
```

## Import
```python
import pandas as pd
from pandas import Series as sr
from pandas import DataFrame as df
```

## Series

```py

myarray = np.arange(9)
myseries = pd.Series(myarray)
myseries

myseries.add(2)
myseries.multiply(2)
pd.Series(map(lambda x: x*2, myseries))

myseries[2]
strSeries = myseries.astype(str)
strSeries[2]

```

```py
myarray = np.array([[1,2,3], [4,5,6]])
mydf = pd.DataFrame(myarray)
mydf
mydf.columns
mydf.columns = ['a', 'b', 'c']
mydf

mydf = pd.DataFrame({'a':[1,2,3],
                     'b':[4,5,6]})

mydf.T
mydf.transpose()

mydf.iloc[:2,1]
mydf.loc[:2, 'a']

mydf['a']
mydf[['a']]
mydf[mydf['a'] < 2]['b']


```

## DataFrame

A data structure with rows & columns, consisting of `pd.Series`

### Create a DataFrame

```python
mydf = pd.DataFrame({'col1': [1, 2, 4,],
                     'col2': 'abc'})


mydf = pd.DataFrame({'col1': [1, 2, 4,],
                     'col2': list('abc')})
```


### Select a Column
```py
a['col1']    # pd.Series
a[['col1']]  # pd.DataFrame
a.col1       # pd.Series

a.col3 = ['d', 'e', 'f']
a.col3
a['col3'] = ['aa', 'bb', 'cc']
a
a[['col3']]
a.col3
```

### Split str and select
```py
DataFrame['col1'].str.split('_').str.get(0)
```

#### Show Unique counts for each columns
```python
DataFrame.apply(lambda x: x.nunique(), axis=0)
```

### Sort values

```python
DataFrame.sort_values(by=['col1', 'col2'], ascending=True)```
```

Drop duplicates keeping last
```py
data = data.drop_duplicates(subset=['col1', 'col2', 'col3'],
                            keep='last')
```

### Select excluding specific columns

```py
DataFrame[DataFrame.columns.difference(['col1', 'col2'])]
```

### words

### Operation
 
```python
codes
```



[↑ Up to the Top](#python-data-manipulation)

---
## datetime
words

### words

### Operation
 
```python
codes
```



[↑ Up to the Top](#python-data-manipulation)

---
## PyTables
words

### words

### Operation
 
```python
codes
```



[↑ Up to the Top](#python-data-manipulation)





---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonProgramming.md)
