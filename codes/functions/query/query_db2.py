def query_db2(query):

    import pandas as pd
    from pandas import DataFrame as df
    import sqlalchemy as sa
    #import ibm_db_sa
    from datetime import datetime as dt

    # DB Connection
    engine = sa.create_engine('ibm_db_sa://username:password@localhost:50000/database', echo=False)
    conn = engine.connect()
    start_tm = dt.now()

    # Get a dataframe[1]
    execonn = engine.execute(query)

    global query_result
    query_result = df(execonn.fetchall())
    query_result.columns = execonn.keys()

    ## Get a dataframe[2]
    #global query_result
    #query_result = pd.read_sql(query, conn)
    #query_result = pd.read_sql(query, engine)

    # Close connection
    end_tm = dt.now()
    print('START :', str(start_tm))
    print(' END  :', str(end_tm))
    print('Elapse:', str(end_tm - start_tm))
    conn.close()
