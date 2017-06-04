[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonDataManipulation.md)


# Numpy

## Installation
```sh
pip install numpy
conda install numpy
```
## Import 
```python
import numpy as np
```


## Create an Array

```py
myarray = np.array([[1,2,3], [4,5,6], [7,8,9]])
myarray

np.identity(3)  # 단위행렬
np.eye(2)  # 단위행렬
np.zeros((3,2))  # 영행렬
np.empty((2,3))  # 영행렬
np.ones((2,2))  # 값이 1인 행렬
np.random.rand(2,3)  # Random 행렬

```

Matrix:
```py
np.matrix(myarray)
```

## Calculation

```py
print(myarray.shape)
print(myarray.dtype)
myarray * 10
myarray + 10

xarray = np.array([[1,2,3], [4,5,6], [7,8,9]])
yarray = np.array([1,0,1])
xarray * yarray
xarray.dot(yarray)
np.dot(xarray, yarray)
```

## Subset

```py
myarray[0][2]
myarray[0,2]
myarray[:2]
myarray[:2,:]
myarray[:,:2]

```

[↑ Up to the Top](#python-data-manipulation)

---


[↑ Up to the Top](#python-data-manipulation)




[↑ Up to the Top](#python-data-manipulation)





---
[← back to *Main Page*](https://github.com/dawkiny/Python3/blob/master/PythonProgramming.md)
