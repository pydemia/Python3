# Built-in Libraries

## ```os```

```python
import os
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |
| ```os.getcwd()```           | return the present working directory            |    ```os.getcwd()```              |
| ```os.chdir(path)```        | change the  working directory to <path>         |    ```os.chdir('~/python')```     |
| ```os.access(path, mode)``` | return ```True/False``` if <mode> can operate in <path>  |    ```os.access('~/python', 'F_OK')```  <br/> 'F_OK': check the path exists  <br/> 'R_OK': check `read` permission  <br/> 'W_OK': check `write` permission  <br/> 'X_OK': check `execute` permission  <br/> 'R_OK': check `read` permission |
| ```os.listdir(path)```      | return a list of files and directories in the <path> or the present working directory            |    ```os.listdir()```              |
| ```os.mkdir(path, mode)```  | create a directory on the given <path> with <mode>  |    ```os.mkdir('~/python/newdir', '0777')```              |
| ```os.makedirs(path, mode)``` | same as 'mkdir -r'; create a directory on the given <path> and subdirectories with <mode>  |    ```os.makedirs('~/python/another/subdir'```      |
| ```os.remove(path)```       | remove the given <path> file               |    ```os.remove('~/python/test.temp')```              |
| ```os.unlink(path)```       | remove the given <path> file                    |    ```os.unlink('~/python/test.temp')```              |
| ```os.rmdir(path)```        | remove the given <path> directory            |    ```os.rmdir('~/python/another/subdir')```              |
| ```os.removedirs(path)```   | same as 'rmdir -r'; remove a directory on the given <path> and subdirectories           |    ```os.rmdir('~/python/another/subdir')```              |
| ```os.rename(src, dst)```   | same as 'mv'; rename or move the given <path> directory or file            |    ```os.rename('~/python/newdir', '~/python/newdirectory')```              |
| ```os.renames(src, dst)```  | same as 'mv -r'; rename or move the given <path> directory or file creating directories if needed           |    ```os.renames('~/python/newdirectory', '~/python/temp/newdirectory')```              |
| ```os.stat(path)```         | get informations of the given <path> directory            |    ```os.stat('~/python')```              |
| ```os.utime(path, times)``` | change the access time and modified time of the given <path>, if <times>=None then now()            |    ```os.utime('~/python')```              |
| ```os.walk(top, topdown=True, onerror=None, followlinks=False)```         | loop startswith the given <top> directory and return pathes and directory names  |    ```os.walk('~/python')```              |
| ```os.getenv(env, failvalue)``` | return the ```environment variable``` if successed or failvalue if failed   |    ```os.getenv('PYTHONPATH', 'Not Found')```              |



## ```sys```

```python
import sys
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |





## ```itertools```

```python
import itertools
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```functools```

```python
import functools
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```string```

```python
import string
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |





## ```datetime```

```python
import datetime
```

Timestamp format:

|Format|Description|
|:-----|:----------|
| ```%Y``` | Year(4 digits) |
| ```%y``` | Year(2 digits) |
| ```%m``` | Month(2 digits) |
| ```%B``` | Month(str) |
| ```%b``` | Month-alias(str) |
| ```%d``` | Day(2 digits) |
| ```%H``` | Hour(24h) |
| ```%I``` | Hour(12h) |
| ```%p``` | AM, PM |
| ```%M``` | Minute(2 digits) |
| ```%S``` | Second(2 digits) |
| ```%f``` | microsecond(6 digits) |
| ```%w``` | Weekday(Int)[0:Sun] |
| ```%A``` | Weekday(str)[0:Sun] |
| ```%a``` | Weekday-alias(str)[0:Sun] |
| ```%U``` | Week(startswith Sun) |
| ```%W``` | Week(startswith Mon) |
| ```%F``` | ```%Y-%m-%d``` |
| ```%D``` | ```%m/%d/%y``` |
| ```%X``` | Locale TimeFormat (```%I:%M:%s %p```) |
| ```%x``` | Locale DateFormat (```%m/%d/%Y```) |


| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |
| ```datetime.datetime.today()```           | return ```datetime``` & ```tzinfo``` of the present ```datetime```            |    ```nowTs = datetime.datetime.today()```              |
| ```datetime.datetime.now()```           | return ```datetime``` of the present ```datetime```            |    ```nowTs = datetime.datetime.now()```              |


#### Types & Objects


class ```timedelta``` :

```python
obj_timedelta = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

| Operation |	Description |
| :-------- | :------- |
|```t1 = t2 + t3```	 | Sum of ```t2``` and ```t3```. </br> Afterwards ```t1-t2 == t3``` and ```t1-t3 == t2``` are ```True```. (1) |
|```t1 = t2 - t3```	 | Difference of ```t2``` and ```t3```. </br> Afterwards ```t1 == t2 - t3``` and ```t2 == t1 + t3``` are ```True```. (1) |
|```t1 = t2 * i``` </br> or ```t1 = i * t2```	 | Delta multiplied by an ```integer```. </br> Afterwards ```t1 // i == t2``` is ```True```, provided ```i != 0```. </br> In general, ```t1 * i == t1 * (i-1) + t1``` is ```True```. (1) |
|```t1 = t2 * f``` </br> or ```t1 = f * t2```	 | Delta multiplied by a ```float```. </br> The result is rounded to the nearest multiple of ```timedelta.resolution``` </br> using round-half-to-even. |
|```f = t2 / t3```	 | Division (3) of ```t2``` by ```t3```. </br> Returns a ```float``` object. |
|```t1 = t2 / f``` </br> or ```t1 = t2 / i```	 | Delta divided by a ```float``` or an ```int```. </br> The result is rounded to the nearest multiple of ```timedelta.resolution``` </br> using round-half-to-even. |
|```t1 = t2 // i``` </br> or ```t1 = t2 // t3```	 | The floor is computed and the remainder (if any) is thrown away. </br> In the second case, an ```integer``` is returned. (3) |
|```t1 = t2 % t3```	 | The remainder is computed as a ```timedelta``` object. (3) |
| ```q, r = divmod(t1, t2)```	 | Computes the quotient and the remainder: </br> ```q = t1 // t2``` (3) and ```r = t1 % t2```. </br> ```q``` is an ```integer``` and ```r``` is a ```timedelta``` object. |
|```+t1```	 | Returns a ```timedelta``` object with the same value. (2) |
|```-t1```	 | equivalent to ```timedelta(-t1.days, -t1.seconds, -t1.microseconds)```,</br> and to ```t1* -1```. (1)(4) |
|```abs(t)```	 | equivalent to ```+t``` when ```t.days >= 0```,</br> and to ```-t``` when ```t.days < 0```. (2) |
|```str(t)```	 | Returns a ```str``` in the form ```[D day[s], ][H]H:MM:SS[.UUUUUU]```, </br> where ```D``` is negative for negative ```t```. (5) |
| ```repr(t)```	 | Returns a ```str``` in the form ```datetime.timedelta(D[, S[, U]])```, </br> where ```D``` is negative for negative ```t```. (5) |


class ```date``` :

```python
obj_date = datetime.date(year, month, day)
```


class ```time``` :

```python
obj_time = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```


class ```datetime``` :

```python
obj_datetime = datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

| Attributes                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |
| ```datetimeObj.fold```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.fold```     |
| ```datetimeObj.min```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.min```     |
| ```datetimeObj.max```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.max```     |
| ```datetimeObj.year```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.year```     |
| ```datetimeObj.month```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.month```     |
| ```datetimeObj.day```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.day```     |
| ```datetimeObj.hour```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.hour```     |
| ```datetimeObj.minute```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.minute```     |
| ```datetimeObj.second```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.second```     |
| ```datetimeObj.microsecond```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.microsecond```     |
| ```datetimeObj.tzinfo```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.tzinfo```     |

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |
| ```datetimeObj.ctime()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.ctime()```     |
| ```datetimeObj.strftime('format')```        | change a ```datetime``` type to ```str```         |    ```nowStr = nowTs.strftime('%Y-%m-%d %H:%M:%S')```     |
| ```datetimeObj.replace(day=self.day, )``` | change a ```str``` type to ```datetime```  |    ```nowTs.replace(year=2016, day=10)``` |
| ```datetimeObj.timetz()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.timetz()```     |
| ```datetimeObj.astimetzone(tz=None)```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.astimezone(tz='EST')```     |
| ```datetimeObj.dst()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.dst()```     |
| ```datetimeObj.tzname()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.tzname()```     |
| ```datetimeObj.timetuple()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.timetuple()```     |
| ```datetimeObj.utctimetuple()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.utctimetuple()```     |
| ```datetimeObj.toordinal()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.toordinal()```     |
| ```datetimeObj.timestamp()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.timestamp()```     |
| ```datetimeObj.weekday()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.weekday()```     |
| ```datetimeObj.isoweekday()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.isoweekday()```     |
| ```datetimeObj.isocalendar()```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.isocalendar()```     |
| ```datetimeObj.isoformat(sep='T', timespec='auto')```        | return a ```str``` from ```datetime```         |    ```nowStr = nowTs.isoformat(sep='T', timespec='auto')```     |

class ```tzinfo``` :

```python
obj_tzinfo = datetime.tzinfo
```


class ```timezone``` :

```python
obj_timezone = datetime.timezone(offset, name=None)
```



## ```math```

```python
import math
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```re```

```python
import re
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```collections```

```python
import collections
```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```tkinter```

```python
import tkinter
```


| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```bisect```

Array bisection algorithm

```python
import bisect
```

| Method                      | Description                                     |
| :-------------------------- | :---------------------------------------------- |
| ```bisect.bisect_left(list, item[, lo[, hi]])```        | Locate the proper insertion point for item in list to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered; by default the entire list is used. If item is already present in list, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first parameter to ```list.insert()```. This assumes that list is already sorted.  |
| ```bisect.bisect_right(list, item[, lo[, hi]])```        | Similar to ```bisect_left()```, but returns an insertion point which comes after (to the right of) any existing entries of item in list.
         |
| ```bisect.bisect(...)```        | Alias for ```bisect.bisect_right(...)```        |
| ```bisect.insort_left(list, item[, lo[, hi]])```        | Insert item in list in sorted order. This is equivalent to ```list.insert(bisect.bisect_left(list, item, lo, hi), item)```. This assumes that list is already sorted.
       |
| ```bisect.insort_right(list, item[, lo[, hi]])```        | Similar to ```insort_left()```, but inserting item in list after any existing entries of item.         |
| ```bisect.insort(...)```        | Alias for ```bisect.insort_right(...)```        |




#### Bisection Algorithm Example

```python
grades = "FEDCBA"
breakpoints = [30, 44, 66, 75, 85]
from bisect import bisect
def grade(total):
    return grades[bisect(breakpoints, total)]

grade(66)
Out[]:
'C'

map(grade, [33, 99, 77, 44, 12, 88])

Out[]:
['E', 'A', 'B', 'D', 'F', 'A']
```

```python
import bisect
def binary_search(A, B):
    clip = lambda idx: max(min(len(A) - 1, idx), 0)
    C = []
    for b in B:
        idx = bisect.bisect(A, b)
        # A[idx-1] < b <= A[idx]
        C.append(closer(A[clip(idx - 1)], A[clip(idx)], b))
    return C
```
