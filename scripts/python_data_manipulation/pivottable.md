# PivotTable & MultiIndex


```panda``` support ```pivot table``` for data manipulation & aggregation.

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
Select & Subset by a index in MultiIndex: 
```python
fcor = corr.xs('EC', level='cd', axis=0).xs('TF', level='cd', axis=1)
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
