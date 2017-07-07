# Python Packaging

## PyPI

### Installation
```sh
python get-pip.py
```

```sh
pip install wheel
pip install twine
```


### PyPI : Create an Account

* [testPyPI](https://testpypi.python.org/pypi)
* [PyPI](https://pypi.python.org/pypi)

#### `~/.pypirc`

```vim
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
#repository=https://pypi.python/pypi
repository:https://upload.pypi.org/legacy/
username=<username>
password=<password>


[testpypi]
#repository=https://testpypi.python/pypi
repository:https://test.pypi.org/legacy/
username=<username>
password=<password>
```


### PyPI : Create a Package

Create `setup.py`:

```sh
cd ~/git/pydemia
vim setup.py

```

```py
from setuptools import setup, find_packages


long_desc = """
This is made for some specific environment.
This contains ...
"""

setup(name='pydemia',
        version='0.0.0.1',
        description='description',
        long_description=long_desc,
        url='http://github.com/pydemia/',
        author='Young Ju Kim',
        author_email='pydemia@gmail.com',
        license='MIT License',
        classifiers=[
                # How Mature: 3 - Alpha, 4 - Beta, 5 - Production/Stable
                'Development Status :: 3 - Alpha',
                'Programming Language :: Python :: 3.5'
                ],
        packages=find_packages(exclude=['contrib', 'docs', 'tests']),
        #install_requires=[],
        zip_safe=False)
```

Create Package Folder:

```sh
mkdir pydemia
vim pydemia/__init__.py
```


### PyPI : Build a Package

```sh
python setup.py sdist bdist_wheel
```


### PyPI : Register a new Package (only at the First time)

```sh
python setup.py register -r https://testpypi.python.org/pypi
python setup.py register -r https://pypi.python.org/pypi
```


### PyPI : Distributte a Package

Note : The name and version of a package is not be overrided.
```sh
twine upload dist/<package>.tar.gz <package>.whl
```

## Conda

### Create a conda Package from PyPI

```sh
conda install
```
