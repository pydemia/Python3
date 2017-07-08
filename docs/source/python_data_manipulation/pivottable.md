# PivotTable & MultiIndex


```panda``` support ```pivot table``` for data manipulation & aggregation.

## Pivot Table(```pandas.pivot_table```, ```pandas.DataFrame.pivot```)

```python
import pandas as pd

pvtbl = pd.pivot_table(data,
                       index=['col1', 'col2'],          # Row index(MultiIndex)
                       columns=[col3', 'col4', 'col5'], # Columns(MultiIndex)
                       values=['col6', 'col7'],         # Column values(Upper level of columns)
                       aggfunc='mean')                  # How to aggregate 
                                                        # if there are multiple records on column group.

```

### Standby a Dataset
```python
from unipy.sample.datasets import dataManager

# Extract Datasets for the first time
dataManager.init()

# Get a Dataset list
dataManager.datalist()

# Load Datasets
aData = dataManager.load('adult')

aData.head()
Out[2]: 
   age          workclass  fnlwgt   education  education_num  \
0   39          State-gov   77516   Bachelors             13   
1   50   Self-emp-not-inc   83311   Bachelors             13   
2   38            Private  215646     HS-grad              9   
3   53            Private  234721        11th              7   
4   28            Private  338409   Bachelors             13   

        marital_status          occupation    relationship    race      sex  \
0        Never-married        Adm-clerical   Not-in-family   White     Male   
1   Married-civ-spouse     Exec-managerial         Husband   White     Male   
2             Divorced   Handlers-cleaners   Not-in-family   White     Male   
3   Married-civ-spouse   Handlers-cleaners         Husband   Black     Male   
4   Married-civ-spouse      Prof-specialty            Wife   Black   Female   

   capital_gain  capital_loss  hours_per_week  native_country  net_capital  
0          2174             0              40   United-States         2174  
1             0             0              13   United-States            0  
2             0             0              40   United-States            0  
3             0             0              40   United-States            0  
4             0             0              40            Cuba            0 


```

```python
aData.info()
```

```py
Out[]:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32561 entries, 0 to 32560
Data columns (total 15 columns):
age               32561 non-null int64
workclass         32561 non-null object
fnlwgt            32561 non-null int64
education         32561 non-null object
education_num     32561 non-null int64
marital_status    32561 non-null object
occupation        32561 non-null object
relationship      32561 non-null object
race              32561 non-null object
sex               32561 non-null object
capital_gain      32561 non-null int64
capital_loss      32561 non-null int64
hours_per_week    32561 non-null int64
native_country    32561 non-null object
net_capital       32561 non-null int64
dtypes: int64(7), object(8)
memory usage: 3.7+ MB

```

```py
aData.apply(lambda x: x.nunique(), axis=0)
```

```py
Out[]:
age                  73
workclass             9
fnlwgt            21648
education            16
education_num        16
marital_status        7
occupation           15
relationship          6
race                  5
sex                   2
capital_gain        119
capital_loss         92
hours_per_week       94
native_country       42
net_capital         210
dtype: int64
```

#### Create a Pivot Table

```python
pvtbl = pd.pivot_table(aData,
                       index=['age'],
                       columns=['sex', 'native_country', 'race'],
                       values='net_capital',
                       aggfunc='mean')

pvtbl.head()
```

```py
Out[]:
sex                         Female                                           \
native_country                   ?                                 Cambodia   
race            Asian-Pac-Islander  Black  Other  White  Asian-Pac-Islander   
age                                                                           
17                             NaN    NaN    NaN    0.0                 NaN   
18                             NaN    NaN    0.0    0.0                 NaN   
19                             NaN    NaN    NaN    0.0                 NaN   
20                             0.0    NaN    NaN    0.0                 NaN   
21                             NaN    NaN    NaN    0.0                 NaN   

sex                                                                           \
native_country                      Canada                      China          
race             Black  Asian-Pac-Islander  White  Asian-Pac-Islander  White   
age                                                                            
17                 NaN                 NaN    NaN                 NaN    NaN   
18             -1602.0                 NaN    NaN                 NaN    NaN   
19                 NaN                 NaN    NaN                 NaN    NaN   
20                 NaN                 NaN    0.0                 NaN    NaN   
21                 NaN                 NaN    NaN                 NaN    NaN   

sex                ...                    Male                             \
native_country     ...         Trinadad&Tobago              United-States   
race               ...      Asian-Pac-Islander  Black  Amer-Indian-Eskimo   
age                ...                                                      
17                 ...                     NaN    NaN                 0.0   
18                 ...                     NaN    NaN                 0.0   
19                 ...                     NaN    NaN                 0.0   
20                 ...                     NaN    NaN                 0.0   
21                 ...                     NaN    NaN                 0.0   

sex                                                                 \
native_country                                                       
race            Asian-Pac-Islander        Black  Other       White   
age                                                                  
17                             NaN     0.000000    0.0    5.164773   
18                             0.0  -123.230769    0.0  185.893617   
19                             0.0     0.000000    0.0  -10.683673   
20                             0.0  1284.777778 -267.0    1.084639   
21                          -658.0    15.758621    0.0    4.379421   

sex                                                    
native_country             Vietnam         Yugoslavia  
race            Asian-Pac-Islander  White       White  
age                                                    
17                             NaN    NaN         NaN  
18                             NaN    NaN         NaN  
19                             0.0    NaN         NaN  
20                             0.0    NaN         0.0  
21                             0.0    NaN         NaN  

[5 rows x 186 columns]
```

## MultiIndex(```pandas.DataFrame.MultiIndex```)

### Add a level to existing `columns` or `levels`

```py
df.columns = pd.MultiIndex.from_product([['NEW_LEVEL'], df.columns])

```

### Select & Subset by `columns`

Select & Subset by a index in MultiIndex: 
```python

DataFrame.xs('col1', level=2, axis=0, drop_level=False)

sbpvt = pvtbl.xs('EC', level='{int | name}', axis=0, drop_level=False) \
             .xs('TF', level='{int | name}', axis=1, drop_level=False)
```

### Flatten MultiIndex `levels`

Flatten a MultiIndex:
```python
pd.DataFrame.columns = pd.DataFrame.columns.tolist()

pd.DataFrame.columns = ['__'.join(t) for t in df.columns]
```

Undo - return a flattened index into MultiIndex

```python
pd.DataFrame.columns = pd.MultiIndex.from_tuples(pd.DataFrames.columns, names={iterables})
```

### Select by `levels`

Get a specific level name list:
```python
pvtbl.columns.get_level_values(3)  # That argument can be a number or level name
pvtbl.volumns.levels(3)
pvtbl.columns.names.index('name')
```

## MultiIndex ```groupby```

Aggregation( axis=column )
```python
pvtbl = pvtbl.groupby(level=list(range(6)), axis=1).agg(max)
```

Fill ( axis=row )
```python
pvtbl = pvtbl.reset_index()
pvtbl = pvtbl.set_index(['col1_fromindex'])
pvtbl = pvtbl.groupby(pvtbl.index).fillna(method='ffill', axis='index')
pvtbl = pvtbl.groupby(pvtbl.index).fillna(method='bfill', axis='index')
pvtbl = pvtbl.set_index(['col2_fromindex'], append=True)
```

## MultiIndex aggregtion by a level
```py
pvtbl = pvtbl.groupby(level=list(pvtbl.columns.names), axis=1).agg(max)
```

### Un-pivot(melt)

```python
pvtbl = pvtbl.reset_index()                             # To keep the data in pivot-table index
melted = pd.melt(pvtbl, id_vars=['col1', 'col2'])       # Un-pivot(melt) the pivot-table
```

Fill ```NaN``` : group by specify columns and re-pivot
```python
melted['value'] = melted.groupby([col3', 'col4'])['value'].apply(lambda x; x.fillna(x.max()))
pvtbl = pd.pivot_table(melted,
                       index=['col1', 'col2'],
                       columns=[col3', 'col4', 'col5'],
                       values=['col6', 'col7'],
                       aggfunc='mean')

```

### Nested ```Groupby```

```Groupby``` specific column levels(axis=1), apply ```replace``` rows(```x```) with ```max(x)```(axis=1):
```python
import numba

fillRows = lambda x: x.fillna(np.max(x))    # define lambda first : 
                                            # numba does not support function creation;lambda
fillRows = lambda x: x.replace(to_replace=x, value=np.max(x))

@numba.jit
def fillRowsbyCols(DataFrame, level_key=None, axis=1):

    res = pd.DataFrame(index=DataFrame.index)
     
    grouped = DataFrame.groupby(level=level_key, axis=axis)
    resDict = dict(list(grouped))
    resKeys = resDict.keys()
    
    for _ in range(len(resDict)):
        keyX = list(resKeys)[_]
        tblX = resDict[keyX]
        tblX = tblX.apply(fillRows, axis=1)
        
        res = pd.concat([res, tblX], axis=1)
    
    res.columns = pd.MultiIndex.from_tuples(res.columns)
    
    return res

DataFrame = fillRowsbyCols(DataFraem, level_key=[], axis=1)
```

This is the same:
```py
DataFrame = DataFrame.groupby(level=[], exis=1).transform(max)
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
