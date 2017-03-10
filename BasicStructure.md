#
```py
mydict = dict.fromkehys(DataFrame.columns)
for _ in mydict:
  mydict[_] = DataFrame[_].index.values.tolist() 

```
