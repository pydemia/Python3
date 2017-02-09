# PivotTable & MultiIndex


```panda``` support ```pivot table``` for data manipulation & aggregation.

## Pivot Table(```pandas.pivot_table```, ```pandas.DataFrame.pivot```)

```python
import pandas as pd

pvtbl = pd.pivot_table(data,
                       index=['col1', 'col2'],            # Row index(MultiIndex)
                       columns=[col3', 'col4', 'col5'],   # Columns(MultiIndex)
                       values=['col6', 'col7'],           # Column values(Upper level of columns)
                       aggfunc='mean')                    # How to aggregate if there are multiple records on column group.

```

### Standby a Dataset
```python
from unipy.sample.datasets import dataManager

# Extract Datasets for the first time
dataManager.init()

# Get a Dataset list
dataManager.datalist()

# Load Datasets
ndata = dataManager.load('nutrients')

ndata.head()
Out[2]: 
     id manufacturer              food_group            foods nutrient_group  \
0  1008          NaN  Dairy and Egg Products  Cheese, caraway    Composition   
1  1008          NaN  Dairy and Egg Products  Cheese, caraway    Composition   
2  1008          NaN  Dairy and Egg Products  Cheese, caraway    Composition   
3  1008          NaN  Dairy and Egg Products  Cheese, caraway          Other   
4  1008          NaN  Dairy and Egg Products  Cheese, caraway         Energy   

                     nutrients units   value  
0                      Protein     g   25.18  
1            Total lipid (fat)     g   29.20  
2  Carbohydrate, by difference     g    3.06  
3                          Ash     g    3.28  
4                       Energy  kcal  376.00  
```


## MultiIndex(```pandas.DataFrame.MultiIndex```)

Select & Subset by a index in MultiIndex: 
```python
fcor = corr.xs('EC', level='{int | name}', axis=0, drop_level=False).xs('TF', level='{int | name}', axis=1, drop_level=False)
```

Flatten a MultiIndex:
```python
pd.DataFrame.columns = pd.DataFrame.columns.tolist()

pd.DataFrame.columns = ['__'.join(t) for t in df.columns]
```

Undo - return a flattened index into MultiIndex

```python
pd.DataFrame.columns = pd.MultiIndex.from_tuples(pd.DataFrames.columns, names={iterables})
```

Get a specific level name list:
```python
pvtbl.columns.get_level_values(3)  # That argument can be a number or level name
```

## Groupby MultiIndex

Aggregation(axis=column)
```python
pvtbl = pvtbl.groupby(level=list(range(6)), axis=1).agg(max)
```

Fill ( axis=row)
```python
pvtbl = pvtbl.reset_index()
pvtbl = pvtbl.set_index(['col1_fromindex'])
pvtbl = pvtbl.groupby(pvtbl.index).fillna(method='ffill', axis='index')
pvtbl = pvtbl.groupby(pvtbl.index).fillna(method='bfill', axis='index')
pvtbl = pvtbl.set_index(['col2_fromindex'], append=True)
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

### MultiIndex Groupby

Groupby specific column levels, apply rows with ```max(x)```:
```python
pvtbl = pvtbl.groupby(level=list(pvtbl.columns.names), axis=1).apply(lambda x: x.fillna(np.max(x)), axis=1)
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
