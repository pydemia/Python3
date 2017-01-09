# Useful Tips

### subset rows on condition(it supports groupby object)
```python
a.col1 = lambda row: np.where(pd.notnull(a.col2)==True, a.col2, a.col3)
```

### groupby key columns, subset rows on condition(by values of calculation with multiple columns)
```python
data = data.groupby(prm_key).filter(lambda x: mape_array(x['col1'], x['col2']) < 3)
```

