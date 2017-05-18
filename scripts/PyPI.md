# PyPI



## Create an Account

### `.pypirc`

```vi
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository=https://pypi.python.pypi
username=<username>
password=<password>


[pypitest]
repository=https://testpypi.python.pypi
username=<username>
password=<password>
```


## Build a Package

```sh
python setup.py sdist bdist_wheel

```

## Distribute it on PyPI

```sh
twine upload dist/<package>.tar.gz
```
