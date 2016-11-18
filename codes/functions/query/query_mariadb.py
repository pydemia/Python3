def query_mariadb(query):

    import pandas as pd
    import pymysql
    from datetime import datetime as dt

    # DB Connection
    conn = pymysql.connect(host='localhost', port='3306', user='username', password='password', database='database')
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
