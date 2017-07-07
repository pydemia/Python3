# Python Packaging

## PyPI

### Installation

Get pip:
```sh
python get-pip.py
```

Get wheel, twine:
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
        install_requires=['pandas>=0.20.2',
                          'pymysql',
                          'psycopg2==2.7.1',
                          'matplotlib>=2.0.2, <2.1.0',],
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

### Installation

```sh
conda install conda-build anaconda-client
```
Then, Create an Account on [Anaconda.org](https://anaconda.org)

### Build a conda Package from PyPI

Note : Not all of PyPI Packages are in conda repository, Your build can be failed with package dependencies.
```sh
conda skeleton pypi <package_name>
conda build <--python 3.5> <package_name>
```
Check it:
```sh
<your-path-to-anaconda>/conda-bld
```
You can see `linux-64`, `osx-64`, `win-64`, etc.

Convert it to other platform:
Linux & OS X:
```sh
conda convert -f --platform all <your-path-to-anaconda>/conda-bld/<your-os>/<your-package-file> -o <outputdir>/
```
Windows:
```sh
conda convert -f --platform all <your-path-to-anaconda>/conda-bld/<your-os>/<your-package-file> -o <outputdir>\
```




### Log-in
```sh
anaconda login

Using Anaconda API: https://api.anaconda.org
Username: pydemia
pydemia's Password: 
login successful

```

### Upload to `Anaconda.org`

```sh
anaconda upload <your-package-name>
```

(Optional) If you want to upload the package at the same time when your build is finished:
```sh
conda config --set anaconda_upload yes
```

### Log-out
```sh
anaconda logout

Using Anaconda API: https://api.anaconda.org
logout successful

```

### Install your Package

```sh
conda install -c <id> <package_name>
```
Done.
