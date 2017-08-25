#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:58:46 2017

@author: pydemia
"""

import numpy as np
import pandas as pd
import unipy as up
import unipy_db as udb

from unipy import time_profiler, job_wrapper

# %%

import pymysql
import asyncio


@time_profiler
async def from_MariaDB(query, h=None, port=3306, db=None, u=None, p=None):

    print('Using MariaDB')

    # DB Connection
    async with pymysql.connect(host=h, port=port, user=u, password=p, database=db) as conn:

        # Get a DataFrame
        await pd.read_sql(query, conn)
        
        query_result = 

        # Close Connection
        conn.close()

    #return query_result

# %%

import pymysql
import asyncio


class Mydb:
    
    async def __aenter__(self):
        self.data = udb.from_MariaDB(self.query, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')
        return self.data
    
    async def __aexit__(self, *args):
        pass
    
    async def __await__(self):
        return self.__aenter__().__await__()
    
    async def query(self, query):
        self.query = query



async def run(query):
    async with Mydb() as obj:
        res = obj.query(query)
        return res

    await Test()

@time_profiler
async def from_MariaDB(query, h=None, port=3306, db=None, u=None, p=None):

    print('Using MariaDB')

    # DB Connection
    async with pymysql.connect(host=h, port=port, user=u, password=p, database=db) as conn:

        # Get a DataFrame
        await pd.read_sql(query, conn)
        
        # Close Connection
        #conn.close()

    #return query_result

# %%
import asyncio
from aiopg.sa import create_engine
import sqlalchemy as sa

metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('val', sa.String(255)))

async def create_table(engine):
    async with engine.acquire() as conn:
        await conn.execute('DROP TABLE IF EXISTS tbl')
        await conn.execute('''CREATE TABLE tbl (
                                  id serial PRIMARY KEY,
                                  val varchar(255))''')

async def go():
    async with create_engine(user='aiopg',
                             database='aiopg',
                             host='127.0.0.1',
                             password='passwd') as engine:

        async with engine.acquire() as conn:
            await conn.execute(tbl.insert().values(val='abc'))

            async for row in conn.execute(tbl.select()):
                print(row.id, row.val)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())

# %%
import asyncio
from functools import partial

getDB_async = partial(from_MariaDB_sa, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')



@job_wrapper
def test_aio_loop(qList):
    bList = [getDB_async(q) for q in qList]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(bList))

res = test_aio_loop(qList)


# %%

import sqlalchemy as sa

@time_profiler
async def from_MariaDB_sa(query, h=None, port=3306, db=None, u=None, p=None):

    print('Using MariaDB')

    # DB Connection
    async with sa.create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(host=h, port=port, user=u, password=p, database=db)) as engine:
        
        async with engine.connect() as conn:

            # Get a DataFrame
            await pd.read_sql(query, conn)
            
        # Close Connection
        conn.close()

    #return query_result


# %%
def getDB_normal(query):
    data = udb.from_MariaDB(query, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')
    return data


async def getDB_async(query):
    data = await from_MariaDB(query, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')
    return data

# %%

def num_fromto_generator(start, end, term):
    pre, nxt = start, start + term -1
    yield pre, nxt
    while nxt < end:
        pre, nxt = nxt, nxt + term
        yield pre+1, nxt

import datetime as dt


def dt_fromto_generator(start, end, day_term, tm_format='%Y%m%d'):
    
    pre = dt.datetime.strptime(start, tm_format)
    term = dt.timedelta(days=day_term)
    nxt = pre + dt.timedelta(days=day_term-1)
    end = dt.datetime.strptime(end, tm_format)
    
    yield pre.strftime(tm_format), nxt.strftime(tm_format)
    
    while nxt < end:
        pre, nxt = nxt, nxt + term
        
        res_pre, res_nxt = pre + dt.timedelta(days=1), nxt
        yield res_pre.strftime(tm_format), res_nxt.strftime(tm_format)


def tm_fromto_generator(start, end, day_term, 
                        tm_string=['000000', '235959'], tm_format='%Y%m%d'):
    
    pre = dt.datetime.strptime(start, tm_format)
    term = dt.timedelta(days=day_term)
    nxt = pre + dt.timedelta(days=day_term-1)
    end = dt.datetime.strptime(end, tm_format)
    
    yield (pre.strftime(tm_format) + tm_string[0],
           nxt.strftime(tm_format) + tm_string[1])
    
    while nxt < end:
        pre, nxt = nxt, nxt + term
        
        res_pre, res_nxt = pre + dt.timedelta(days=1), nxt
        yield (res_pre.strftime(tm_format) + tm_string[0],
               res_nxt.strftime(tm_format) + tm_string[1])



# %%
queryStr = """
SELECT *
FROM employees.employees
WHERE EMP_NO BETWEEN {pre} AND {nxt}
;
"""

qList = [queryStr.format(pre=item[0], nxt=item[1])
         for item in num_fromto_generator(10001, 300000, 100000)]
qList = [queryStr.format(pre=10001, nxt=300001) for i in range(10)]

# %%

dtList = [item for item in dt_fromto_generator('20170101','20170331', 10)]
tmList = [item for item in tm_fromto_generator('20170101','20170331', 10)]
# %% Normal Loop
    
aList = [getDB_normal(q) for q in qList]

# %%

import asyncio
from functools import partial

getDB_async = partial(from_MariaDB_sa, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')



@job_wrapper
def test_aio_loop(qList):
    bList = [getDB_async(q) for q in qList]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(bList))

res = test_aio_loop(qList)

# %%

def get_task():
    loop = asyncio.get_event_loop()
    try:
        return asyncio.Task.get_current(loop)
    except RuntimeError:
        return None

asyncio.Task.get_
get_task()
# %% Async Loop : 49 over

import asyncio

bList = [getDB_async(q) for q in qList]

@job_wrapper
def test_aio_loop():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(bList))

res = test_aio_loop()

# %%
async def run_async_main(qList):
    
    future = [asyncio.ensure_future(getDB_async(q)) for q in qList]
    result = await asyncio.gather(*future)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_async_main(qList))

# %% Async Loop : 49 over

import asyncio

bList = [getDB_async(q) for q in qList]

from functools import partial

getDB_test = partial(udb.from_MariaDB, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')


async def getDB_async(query):
    
    loop = asyncio.get_event_loop()
    data1 = await loop.run_in_executor(None, getDB_test, )
    return data


async def run_async_main(qList):
    
    future = [asyncio.ensure_future(getDB_async(q)) for q in qList]
    result = await asyncio.gather(*future)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_async_main())
#loop.close() 

#@job_wrapper
#def test_aio_loop():
#    
#    loop = asyncio.get_event_loop()
#    res = loop.run_until_complete(run_async_main())
#    loop.close() 
#    return res
#
#res = test_aio_loop()
# %%

# %%

async def getDB_async_unit(query):
    data = await udb.from_MariaDB(query, h='windows.pydemia.org', port=3306, db='employees', u='mdb', p='mdb')
    return [data]


@asyncio.coroutine
def run_parallel3():
    tasks = [asyncio.async(getDB_async_unit(q)) for q in qList]
    done, pending = yield from asyncio.wait(tasks)
    # Results will NOT necessarily be in the order called
    results = [future.result() for future in done]
    print("Results3: {}".format(results))

loop = asyncio.get_event_loop()
#loop.run_until_complete(run_parallel())
#loop.run_until_complete(run_parallel2())
loop.run_until_complete(run_parallel3())
#loop.close()


# %%
import asyncio
from urllib.request import urlopen

@asyncio.coroutine
def print_data_size():
   data = yield from get_data_size()
   print("Data size: {}".format(data))

# Note that this is a synchronous function
def sync_get_url(url):
   return urlopen(url).read()

@asyncio.coroutine
def get_data_size():
   loop = asyncio.get_event_loop()

   # These each run in their own thread (in parallel)
   future1 = loop.run_in_executor(None, sync_get_url, 'http://xkcd.com')
   future2 = loop.run_in_executor(None, sync_get_url, 'http://google.com')

   # While the synchronous code above is running in other threads, the event loop
   # can go do other things.
   data1 = yield from future1
   data2 = yield from future2
   return len(data1) + len(data2)

loop = asyncio.get_event_loop()
loop.run_until_complete(print_data_size())

# %%

import asyncio

@asyncio.coroutine
def waitn(n):
    asyncio.sleep(n)
    return "I waited {}".format(n)

@asyncio.coroutine
def run_parallel():
    # Results will be in order called
    results = yield from asyncio.gather(waitn(3), waitn(1), waitn(2))
    print("Results: {}".format(results))

@asyncio.coroutine
def run_parallel2():
    tasks = [waitn(i) for i in (3,1,2)]
    # Results will be in order called
    results = yield from asyncio.gather(*tasks)
    print("Results2: {}".format(results))

@asyncio.coroutine
def run_parallel3():
    tasks = [asyncio.async(waitn(i)) for i in (3,1,2)]
    done, pending = yield from asyncio.wait(tasks)
    # Results will NOT necessarily be in the order called
    results = [future.result() for future in done]
    print("Results3: {}".format(results))

loop = asyncio.get_event_loop()
loop.run_until_complete(run_parallel())
loop.run_until_complete(run_parallel2())
loop.run_until_complete(run_parallel3())
#loop.close()

# %%

from time import time
from urllib.request import Request, urlopen
import asyncio
 
urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]
 
async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})    # UA가 없으면 403 에러 발생
    response = await loop.run_in_executor(None, urlopen, request)    # run_in_executor 사용
    page = await loop.run_in_executor(None, response.read)           # run in executor 사용
    return len(page)
 
async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
                                                           # 태스크(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures)                # 결과를 한꺼번에 가져옴
    print(result)
 
begin = time()
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
#loop.close()                             # 이벤트 루프를 닫음
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))
# %% Multi-Processing : 19sec 

import multiprocessing

from functools import partial
jobwrap = partial(job_wrapper, 'test_mp')


@job_wrapper
def test_mp():
    pool = multiprocessing.pool.Pool(processes=len(qList))
    response = pool.map(getDB_normal, qList, chunksize=1)
    
    return response

res = test_mp()
    
# %% Multi-Threading : 56sec

import multiprocessing


@job_wrapper
def test_mt():
    pool = multiprocessing.pool.ThreadPool(processes=4)
    response = pool.map(getDB_normal, qList, chunksize=1)
    
    return response

res = test_mt()

# %%

def coro():
    hello = yield "Hello"
    yield hello
 
 
c = coro()
print(next(c))
print(c.send("World"))



# %%

def a_job(num, start, end):
    
    print('%d JobStart' % num)
    res = []
    for i in range(start, end+1):
        res.append(i)
    print('%d JobEnd' % num)
    return res

a = list(range(1, 20))
b = list(range(1, 20))
c = list(range(1000000, 1000020))
res = up.multiprocessor(a_job, processes=5, arg_zip=zip(a, b, c))


# %% asyncio

import asyncio

def async_job()
