# PyPI


```sh
pip install wheel
pip install twine
```


## Create an Account

### `~/.pypirc`

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


## Create an Package

Create `setup.py`:

```sh
cd ~/git/pydemia
vim setup.py

```

```vi
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


## Build a Package

```sh
python setup.py sdist bdist_wheel

```

## Distribute it on PyPI

```sh
twine upload dist/<package>.tar.gz
```
