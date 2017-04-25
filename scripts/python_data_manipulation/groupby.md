[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonDataManipulation.md)


# ```pandas.DataFrame.groupby```

It is for 'split - apply - combine' operation.

## Standby a Dataset
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

### groupby object(split)

It's an compressed object from ```DataFrame```,  grouped(splitted) by a given index(usually its column index).
```python
grp = ndata.groupby('food_group')
grp
Out[]: 
 <pandas.core.groupby.DataFrameGroupBy object at 0x7f4f95fa5470>
```

You can create it by multiple indices.
```python
grp = ndata.groupby(['food_group', 'foods'])
grp
Out[]: 
<pandas.core.groupby.DataFrameGroupBy object at 0x7f4f95f82160>
```

And you can change its exis:
```python
grp = ndata.groupby(['id'], axis=1)
grp
Out[]: 
<pandas.core.groupby.DataFrameGroupBy object at 0x7f4f9542e748>
```

and more: functions(len, ...), MultiIndex(level='', axis=1)


### groupby operation(apply and combine)

you can apply some functions for each groups splitted by the given index.
```python
ndata.groupby(['food_group', 'foods']).mean()[:5]
Out[]: 
                                                              id      value
food_group foods                                                           
Baby Foods Baby food, fortified cereal bar, fruit filling   3964  74.455483
           Babyfood, apple yogurt dessert, strained        42150  17.194431
           Babyfood, apple-cranberry juice                  3169  11.611923
           Babyfood, apples with ham, strained              3289  12.816692
           Babyfood, baked product, finger snacks cereal   42284  88.900680
```

In this case, we applied a function ```mean()``` to the columns its dtype is ```numeric```.  
but ```id``` column looks like not-calculated because it has the unique value for each groups and represents the foods by number.  

You can appoint a column. like ```DataFrame```, you can subset columns to operate.  
```python
ndata.groupby(['food_group', 'foods'])['id'].mean()[:5]
Out[]: 
food_group  foods                                         
Baby Foods  Baby food, fortified cereal bar, fruit filling     3964
            Babyfood, apple yogurt dessert, strained          42150
            Babyfood, apple-cranberry juice                    3169
            Babyfood, apples with ham, strained                3289
            Babyfood, baked product, finger snacks cereal     42284
```


The results of the above have ```MultiIndex```(Hierachical Index).  

### Iterate for each group

```python
i = 1

for name, group in ndata.groupby(['food_group', 'foods']):
    
    while i < 3:
        i += 1
        print(name)
        
        print(group[:3])

('Baby Foods', 'Baby food, fortified cereal bar, fruit filling')
         id manufacturer  food_group  \
30613  3964          NaN  Baby Foods   
30614  3964          NaN  Baby Foods   
30615  3964          NaN  Baby Foods   

                                                foods nutrient_group  \
30613  Baby food, fortified cereal bar, fruit filling    Composition   
30614  Baby food, fortified cereal bar, fruit filling    Composition   
30615  Baby food, fortified cereal bar, fruit filling    Composition   

                         nutrients units  value  
30613                      Protein     g   5.43  
30614            Total lipid (fat)     g   5.30  
30615  Carbohydrate, by difference     g  68.63  
('Baby Foods', 'Baby food, fortified cereal bar, fruit filling')
         id manufacturer  food_group  \
30613  3964          NaN  Baby Foods   
30614  3964          NaN  Baby Foods   
30615  3964          NaN  Baby Foods   

                                                foods nutrient_group  \
30613  Baby food, fortified cereal bar, fruit filling    Composition   
30614  Baby food, fortified cereal bar, fruit filling    Composition   
30615  Baby food, fortified cereal bar, fruit filling    Composition   

                         nutrients units  value  
30613                      Protein     g   5.43  
30614            Total lipid (fat)     g   5.30  
30615  Carbohydrate, by difference     g  68.63  
```

You can pick a group from the groupby object.
```python
pick = dict(list(ndata.groupby(['food_group', 'foods'])))
keys = list(pick.keys())
keys[:3]

Out[]: 
[('Legumes and Legume Products',
  'MORNINGSTAR FARMS Veggie Breakfast Bacon Strips, frozen, unprepared'),
 ('Fast Foods', "McDONALD'S, QUARTER POUNDER with Cheese"),
 ('Poultry Products',
  'Chicken, broilers or fryers, leg, meat only, cooked, stewed')]
  
pick[keys[0]][:5]
Out[]: 
           id  manufacturer                   food_group  \
179737  16542  Kellogg, Co.  Legumes and Legume Products   
179738  16542  Kellogg, Co.  Legumes and Legume Products   
179739  16542  Kellogg, Co.  Legumes and Legume Products   
179740  16542  Kellogg, Co.  Legumes and Legume Products   
179741  16542  Kellogg, Co.  Legumes and Legume Products   

                                                    foods nutrient_group  \
179737  MORNINGSTAR FARMS Veggie Breakfast Bacon Strip...    Composition   
179738  MORNINGSTAR FARMS Veggie Breakfast Bacon Strip...    Composition   
179739  MORNINGSTAR FARMS Veggie Breakfast Bacon Strip...    Composition   
179740  MORNINGSTAR FARMS Veggie Breakfast Bacon Strip...          Other   
179741  MORNINGSTAR FARMS Veggie Breakfast Bacon Strip...         Energy   

                          nutrients units  value  
179737                      Protein     g   12.4  
179738            Total lipid (fat)     g   26.6  
179739  Carbohydrate, by difference     g   14.3  
179740                          Ash     g    4.8  
179741                       Energy  kcal  346.0  
```

describe()
```python
data.groupby(key).describe()
```

### advanced operations

agg()
```python
data.groupby(key).agg({'col1': np.max, 'col2': 'sum', 'col3': ['sum', 'min', 'max', 'std']})
```
It looks like the result of ```describe()```.

transform()
return a new resut ```DataFrame```
```python
data.groupby(key).transform(np.mean())
```

filter()
```python
data.groupby(key).filter(lambda x: len(x['col'].dropna()) >= 10)
data.groupby(key).filter(lambda x: len(x['col'].std() != 0)
```



### Groupby apply a function
apply

If you want to fill ```NaN``` with the mean values for each group:
```python
data.groupby(key)[value_column].apply(lambda x: x.fillna(x.mean())
```

To create a column of the weighted averages for each group:
```python
data['newcol'] = data.groupby(key)[value_column].apply(lambda x: np.average(x['value_column'], weights=x['weights'])
```

Use `apply` to use indirect Function:
```py
DataFrame.groupby(key).fillna(method='ffill', axis=0)
DataFrame.groupby(key).apply(lambda grp:grp.interpolate(method='values', axis=0))

```


Groupby OLS:
```python
import statsmodels.api as sm
def regress(data, yvar, xvars):

    y = data[yvar]
    X = data[xvars]
    
    X['intercept'] = 1.
    res = sm.OLS(y, X).fit()
    return res.params

data.groupby(key).apply(regress, yvar, xvars)
```


### Groupby Iteration

```py
ndata = dm.load('nutrients')
ndata.columns
grouped = ndata.groupby(['nutrients'])
for key, value in grouped['value']:
    print(key, value.max())
```

[↑ Up to the Top](#python-data-manipulation)





---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonProgramming.md)
