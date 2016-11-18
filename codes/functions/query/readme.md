# Query_Examples

## PostgreSQL
```sql
SELECT *
FROM database.table
WHERE 1=1
AND time BETWEEN 20160101 and 20161231
LIMIT 10
;
```

## IBM_DB2
```sql
SELECT *
FROM database.table
WHERE 1=1
AND time BETWEEN 20160101 and 20161231
FETCH FIRST 10 ROWS ONLY
WITH UR
;
```

## Oracle
```sql
SELECT *
FROM table
WHERE 1=1
AND field1 LIKE 'str%'
AND time BETWEEN
    to_date('2016-01-01T00:00:00', 'YYYY-MM-DD"T"HH24:MI:SS')
    and
    to_date('2016-12-31T23:59:59', 'YYYY-MM-DD"T"HH24:MI:SS')
AND ROWNUM <= 10
;
```

## MariaDB
