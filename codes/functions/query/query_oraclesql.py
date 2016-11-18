def query_oraclesql(query):

    import pandas as pd
    import cx_Oracle as co
    from datetime import datetime as dt

    # DB Connection
    dnsStr = co.makedsn('localhost', '1521', 'database')
    dnsStr = dsnStr.replace('SID', 'SERVICE_NAME')
    conn = co.connect('username', 'password', dnsStr)
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
