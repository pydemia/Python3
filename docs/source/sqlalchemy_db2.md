#SQLAlchemy
```sh
conda install sqlalchemy
```

#DB2

```sh
conda install ibm_db
conda install ibm_db_sa
```

```python
import sqlalchemy as sa
#import ibm_db_sa
import pandas as pd
from pandas import DataFrame as df

db2 = sa.create_engine('ibm_db_sa://user:passwd@ipadress:port/dbname', echo=True)
conn = db2.connect()

sql_str = """
SELECT *
FROM ~
WHERE ~
AND ~
FETCH FIRST 2 ROWS ONLY
WITH UR
"""

# Send a query
query = db2.execute(sql_str)

# Transform query to df
res = df(query.fetchall()
res.columns = query.keys()
```
