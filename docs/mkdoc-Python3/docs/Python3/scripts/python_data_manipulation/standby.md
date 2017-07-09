[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/Readme.md)


# Standby Datasets

* [Adult(UCI)](#numpy)  
* [Wine Quality(UCI)](#pandas)  
* [Food Nutrients(USDA)](#datetime)  


## Food Nutrients

```json``` to ```csv```
```python
import json
import numpy as np
import pandas as pd
db = json.load(open('foods-2011-10-03.json'))

nutrients = pd.DataFrame(db[0]['nutrients'])
info_keys = ['description', 'group', 'id', 'manufacturer']
info = pd.DataFrame(db, columns=info_keys)

nutrients = []
for rec in db:
    fnuts = pd.DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)

col_map = {'description': 'foods', 'group': 'food_group'}
info = info.rename(columns=col_map, copy=False)

col_map = {'description': 'nutrients', 'group': 'nutrient_group'}
nutrients = nutrients.rename(columns=col_map, copy=False)

ndata = pd.merge(nutrients, info, on='id', how='outer')

ndata.manufacturer = np.where(ndata.manufacturer == '',
                              np.NaN, ndata.manufacturer)


ndata = ndata[['id', 'manufacturer', 'food_group', 'foods',
               'nutrient_group', 'nutrients', 'units', 'value']]

ndata.to_csv('nutrients.data', sep=',', header=True, index=False)
```

```python
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

---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonProgramming.md)
