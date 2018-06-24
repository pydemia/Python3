
# Sphinx


### `.rst`

```sh
pip install sphinx sphinx-autobuild
```

```sh
cd ~/git/unipy
sphinx-quickstart
```

```sh
Welcome to the Sphinx 1.7.5 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:

The project name will occur in several places in the built documentation.
> Project name: unipy
> Author name(s): Young Ju Kim
> Project release []: 0.0.4.19

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]:

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]: n
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: y
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: y
> Create Windows command file? (y/n) [y]: n

Creating file ./conf.py.
Creating file ./index.rst.
Creating file ./Makefile.

Finished: An initial directory structure has been created.

You should now populate your master file ./index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

```

Then, edit `index.rst` and `conf.py`.

```sh
vim docs/conf.py
```

```py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from unipy import __version__

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon']

source_suffix = ['.rst', '.md']

# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

```

```sh
sphinx-apidoc -F -o ./ ../unipy/ --separate

```

```sh
Creating file ./unipy.rst.
Creating file ./unipy.core.api.rst.
Creating file ./unipy.core.rst.
Creating file ./unipy.dataset.api.rst.
Creating file ./unipy.dataset.rst.
Creating file ./unipy.image.api.rst.
Creating file ./unipy.image.houghmatrix.rst.
Creating file ./unipy.image.rst.
Creating file ./unipy.math.api.rst.
Creating file ./unipy.math.geometry.rst.
Creating file ./unipy.math.rst.
Creating file ./unipy.plots.api.rst.
Creating file ./unipy.plots.boxplot.rst.
Creating file ./unipy.plots.rst.
Creating file ./unipy.stats.api.rst.
Creating file ./unipy.stats.feature_selection.rst.
Creating file ./unipy.stats.formula.rst.
Creating file ./unipy.stats.hypo_test.rst.
Creating file ./unipy.stats.metrics.rst.
Creating file ./unipy.stats.rst.
Creating file ./unipy.tools.api.rst.
Creating file ./unipy.tools.data_handler.rst.
Creating file ./unipy.tools.rst.
Creating file ./unipy.unipy_test.test_data_handler.rst.
Creating file ./unipy.unipy_test.test_dataset.rst.
Creating file ./unipy.unipy_test.test_example.rst.
Creating file ./unipy.unipy_test.test_hypothesis.rst.
Creating file ./unipy.unipy_test.test_samplecode.rst.
Creating file ./unipy.unipy_test.test_stats.rst.
Creating file ./unipy.unipy_test.rst.
Creating file ./unipy.utils.api.rst.
Creating file ./unipy.utils.decorator.rst.
Creating file ./unipy.utils.gdrive.rst.
Creating file ./unipy.utils.generator.rst.
Creating file ./unipy.utils.remote_ipyconnector.rst.
Creating file ./unipy.utils.wrapper.rst.
Creating file ./unipy.utils.rst.
File ./conf.py already exists, skipping.
File ./index.rst already exists, skipping.
File ./Makefile already exists, skipping.
Creating file ./make.bat.
```

Build `C Extension` first or reinstall `pandas`, for avoiding this:
```sh
Running Sphinx v1.7.5

Configuration error:
There is a programable error in your configuration file:

Traceback (most recent call last):
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/pandas/__init__.py", line 26, in <module>
    from pandas._libs import (hashtable as _hashtable,
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/pandas/_libs/__init__.py", line 4, in <module>
    from .tslib import iNaT, NaT, Timestamp, Timedelta, OutOfBoundsDatetime
  File "pandas/_libs/tslibs/conversion.pxd", line 11, in init pandas._libs.tslib
ModuleNotFoundError: No module named 'pandas._libs.tslibs.conversion'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/sphinx/config.py", line 161, in __init__
    execfile_(filename, config)
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/sphinx/util/pycompat.py", line 150, in execfile_
    exec_(code, _globals)
  File "conf.py", line 23, in <module>
    from unipy import __version__
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/unipy/__init__.py", line 14, in <module>
    from unipy import math
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/unipy/math/__init__.py", line 9, in <module>
    from unipy.math import geometry
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/unipy/math/geometry.py", line 10, in <module>
    import pandas as pd
  File "/home/pydemia/apps/anaconda3/lib/python3.6/site-packages/pandas/__init__.py", line 35, in <module>
    "the C extensions first.".format(module))
ImportError: C extension: No module named 'pandas._libs.tslibs.conversion' not built. If you want to import pandas from the source directory, you may need to run 'python setup.py build_ext --inplace --force' to build the C extensions first.

Makefile:20: recipe for target 'html' failed
make: *** [html] Error 2
```

```sh
cd ~git/unipy
python setup.py build_ext --inplace --force
```


```sh
cd docs
make html
```

For `ImportError: 'opentype'`:

```py
pip install pyasn1 pyasn1-modules
pip install --upgrade google-auth-oauthlib
pip install --upgrade pyasn1-modules
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
