# Python SQL(RDBMS)


## SELECT & EXPORT TO DataFrame

### IBM_DB2 (```sqlalchemy```, ```fetchall()```)

```py
import pandas as pd
import sqlalchemy as sa
from datetime import datetime


def db2SQL(query, h=None, port=None, db=None, u=None, p=None):

    print('Using IBM DB2')

    # DB Connection
    connStr = 'ibm_db_sa://{}:{}@{}:{}/{}'
    engine = sa.create_engine(connStr.format(u, p, h, str(port), db))
    conn = engine.connect()
    start_tm = datetime.now()
    print(' Start :', str(start_tm))

    # Get a DataFrame
    execonn = engine.execute(query)

    query_result = pd.DataFrame(execonn.fetchall())
    query_result.columns = execonn.keys()

    # Close Connection
    end_tm = datetime.now()
    print(' Finish :', str(end_tm))
    print('Elapsed :', str(end_tm - start_tm))
    conn.close()

    return query_result

```

### PostgreSQL (```psycopg2```)

```py
import pandas as pd
import psycopg2 as pg
from datetime import datetime 


def postgreSQL(query, h=None, port=None, db=None, u=None, p=None):

    print('Using PostgreSQL')

    # DB Connection
    conn = pg.connect(host=h, port=str(port), user=u, password=p)
    start_tm = datetime.now()
    print(' Start :', str(start_tm))

    # Get a DataFrame
    query_result = pd.read_sql(query, conn)

    # Cloase Connection
    end_tm = datetime.now()
    print(' Finish :', str(end_tm))
    print('Elapsed :', str(end_tm - start_tm))
    conn.close()

    return query_result
```


### MySQL(MariaDB)(```pymysql```)

```py
import pandas as pd
import pymysql
from datetime import datetime 


def mariaDB(query, h=None, port=None, db=None, u=None, p=None):

    print('Using MariaDB')

    # DB Connection
    conn = pymysql.connect(host=h, port=p, user=u, password=p, database=db)
    start_tm = datetime.now()
    print(' Start :', str(start_tm))

    # Get a DataFrame
    query_result = pd.read_sql(query, conn)

    # Close Connection
    end_tm = datetime.now()
    print(' Finish :', str(end_tm))
    print('Elapsed :', str(end_tm - start_tm))
    conn.close()

    return query_result
```

### OracleSQL (```cx_Oracle```)

```py
import pandas as pd
import cx_Oracle as co        # IF error, THEN install OracleDB
from datetime import datetime


def oracleSQL(query, h=None, port=None, db=None, u=None, p=None):

    print('Using OracleDB')

    # DB Connection
    dnsStr = co.makedsn(h, str(port), db)
    dnsStr = dnsStr.replace('SID', 'SERVICE_NAME')
    conn = co.connect(u, p, dnsStr)
    start_tm = datetime.now()

    # Get a DataFrame
    query_result = pd.read_sql(query, conn)

    # Close Connection
    end_tm = datetime.now()
    print(' Finish :', str(end_tm))
    print('Elapsed :', str(end_tm - start_tm))
    conn.close()

    return query_result
```

## IMPORT DataFrame to DB

### MySQL(MariaDB)(```sqlalchemy```)

```py
import pandas as pd
import sqlalchemy as sa
from datetime import datetime


def mariaDB(dataframe, name=None, h=None, port=None, db=None, u=None, p=None,
            if_exists='append'):

    print('Using MariaDB')

    # DB Connection
    connStr = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
    engine = sa.create_engine(connStr.format(u, p, h, str(port), db))
    conn = engine.connect()
    start_tm = datetime.now()
    print(' Start :', str(start_tm))

    # Get a DataFrame
    dataframe.to_sql(con=conn, name=None, if_exists=if_exists,
                     flavor='mysql', index=False, chunksize=None)

    # Close Connection
    end_tm = datetime.now()
    print(' Finish :', str(end_tm))
    print('Elapsed :', str(end_tm - start_tm))
    conn.close()

```
