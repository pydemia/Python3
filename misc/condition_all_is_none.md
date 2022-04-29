```py
a = None
b = None
c = None
if not any(map(None.__ne__, (a, b, c))):
    print("all is None")
else:
    print("any is not None")
```

```py
all is None
```


```py
a = 1
b = None
c = None
if not any(map(None.__ne__, (a, b, c))):
    print("all is None")
else:
    print("any is not None")
```

```py
any is not None
```
