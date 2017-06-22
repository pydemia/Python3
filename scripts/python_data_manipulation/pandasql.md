# `pandasql`

## Installation

```sh
pip install pandasql
conda install pandasql
```

## Import

```py
import pandasql as ps
from pandasql import sqldf

```

## Usage

```py
from unipy.sample.datasets import dataManager

data1 = dataManager.load(0)
data2 = dataManager.load(1)
```

```py
from pandasql import load_meat, load_births

meat = load_meat()
births = load_births()

meat.head()
births.head()
```

```py
import pandas as pd
import matplotlib.pyplot as plt

pysqldf = lambda q: sqldf(q, globals())  # global() within script, local() within local namespaces

queryStr = """

SELECT
  m.date
  , m.beef
  , b.births
FROM
  meat m
LEFT JOIN
  births b
    ON m.date = b.date
WHERE
    m.date > '1974-12-31'
;

"""

res = pysqldf(queryStr)
res.head()

```
