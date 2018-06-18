
# Sphinx


### `.rst`

```sh
pip install sphinx sphinx-autobuild
```

```sh
cd ~/git/unipy
mkdir docs
cd docs
sphinx-quickstart
```

```sh

```
Then, edit `index.rst` and `conf.py`.

```sh
make html
```


## `.md`

```sh
pip install recommonmark
```

```sh
cd ~/git/unipy
mkdir docs
cd docs
sphinx-quickstart
```

```sh

```
Then, edit `index.rst` and `conf.py`.


* `conf.py`
```py
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

```

```sh
make html
```
