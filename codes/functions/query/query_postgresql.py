def query_postgresql(query_str):

    import pandas as pd
    import psycopg2 as pg
    from datetime import datetime as dt

    # DB Connection
    conn = pg.connect(host='localhost', port='5432', dbname='database', user='username', password='password')
    start_tm = dt.now()

    # Get a dataframe
    global query_result
    query_result = pd.read_sql(query, conn)

    # Close connection
    end_tm = dt.now()
    print('START :', str(start_tm))
    print(' END  :', str(end_tm))
    print('Elapse:', str(end_tm - start_tm))
    conn.close()
