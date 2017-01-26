# Built-in Libraries

## ```os```

```import os```


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

```import sys```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |





## ```itertools```

```import itertools```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```functools```

```import functools```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```string```

```import string```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |





## ```datetime```

```import datetime```

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
| ```%F``` | %Y-%m-%d |
| ```%D``` | %m/%d/%y |
| ```%X``` | Locale TimeFormat (%I:%M:%s %p) |
| ```%x``` | Locale DateFormat (%m/%d/%Y) |

#### Types & Objects

```timedelta```:
```python
obj_timedelta = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

```date```:
```python
obj_date = datetime.date(year, month, day)
```


```datetime```:
```python
obj_datetime = datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```


```time```:
```python
obj_time = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```


```tzinfo```:
```python
obj_tzinfo = datetime.tzinfo
```


```timezone```:
```python
obj_timezone = datetime.timezone(offset, name=None)
```


| Operation |	Result |
|```t1 = t2 + t3```	Sum of ```t2``` and ```t3```. Afterwards ```t1-t2 == t3``` and ```t1-t3 == t2``` are ```True```. (1)
|```t1 = t2 - t3```	Difference of ```t2``` and ```t3```. Afterwards ```t1 == t2 - t3``` and ```t2 == t1 + t3``` are ```True```. (1)
|```t1 = t2 * i``` or ```t1 = i * t2```	Delta multiplied by an ```integer```. Afterwards ```t1 // i == t2``` is ```True```, provided ```i != 0```. </br> In general, ```t1 * i == t1 * (i-1) + t1``` is ```True```. (1)
|```t1 = t2 * f or t1 = f * t2```	Delta multiplied by a ```float```. The result is rounded to the nearest multiple of ```timedelta.resolution``` using round-half-to-even.
|```f = t2 / t3	Division``` (3) of ```t2``` by ```t3```. Returns a ```float``` object.
|```t1 = t2 / f``` or ```t1 = t2 / i```	Delta divided by a ```float``` or an ```int```. The result is rounded to the nearest multiple of ```timedelta```.resolution using round-half-to-even.
|```t1 = t2 // i``` or ```t1 = t2 // t3```	The floor is computed and the remainder (if any) is thrown away. In the second case, an ```integer``` is returned. (3)
|```t1 = t2 % t3```	The remainder is computed as a ```timedelta``` object. (3)
| ```q, r = divmod(t1, t2)```	Computes the quotient and the remainder: ```q = t1 // t2``` (3) and ```r = t1 % t2```. q is an ```integer``` and ```r``` is a ```timedelta``` object.
|```+t1```	Returns a ```timedelta``` object with the same value. (2)
|```-t1```	equivalent to ```timedelta(-t1.days, -t1.seconds, -t1.microseconds)```, and to ```t1* -1```. (1)(4)
|```abs(t)```	equivalent to ```+t``` when ```t.days >= 0```, and to ```-t``` when ```t.days < 0```. (2)
|```str(t)```	Returns a ```str``` in the form ```[D day[s], ][H]H:MM:SS[.UUUUUU]```, where ```D``` is negative for negative ```t```. (5)
| ```repr(t)```	Returns a ```str``` in the form ```datetime.timedelta(D[, S[, U]])```, where ```D``` is negative for negative ```t```. (5)


| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |
| ```datetime.datetime.now()```           | return Timestamp of the present datetime            |    ```nowTs = datetime.datetime.now()```              |
| ```Timestamp.strftime('format')```        | change a Timestamp type to str         |    ```nowStr = nowTs.strftime('%Y-%m-%d %H:%M:%S')```     |
| ```Timestamp.replace(str, 'format')``` | change a str type to Timestamp  |    ```datetime.datetime.strptime(nowStr, '%Y-%m-%d %H:%M:%S')``` |
| ```datetime.listdir(path)```      | return a list of files and directories in the <path> or the present working directory            |    ```datetime.listdir()```              |
| ```datetime.mkdir(path, mode)```  | create a directory on the given <path> with <mode>  |    ```datetime.mkdir('~/python/newdir', '0777')```              |
| ```datetime.makedirs(path, mode)``` | same as 'mkdir -r'; create a directory on the given <path> and subdirectories with <mode>  |    ```datetime.makedirs('~/python/another/subdir'```      |
| ```datetime.remove(path)```       | remove the given <path> file               |    ```datetime.remove('~/python/test.temp')```              |
| ```datetime.unlink(path)```       | remove the given <path> file                    |    ```datetime.unlink('~/python/test.temp')```              |
| ```datetime.rmdir(path)```        | remove the given <path> directory            |    ```datetime.rmdir('~/python/another/subdir')```              |
| ```datetime.removedirs(path)```   | same as 'rmdir -r'; remove a directory on the given <path> and subdirectories           |    ```datetime.rmdir('~/python/another/subdir')```              |
| ```datetime.rename(src, dst)```   | same as 'mv'; rename or move the given <path> directory or file            |    ```datetime.rename('~/python/newdir', '~/python/newdirectory')```              |
| ```datetime.renames(src, dst)```  | same as 'mv -r'; rename or move the given <path> directory or file creating directories if needed           |    ```datetime.renames('~/python/newdirectory', '~/python/temp/newdirectory')```              |
| ```datetime.stat(path)```         | get informations of the given <path> directory            |    ```datetime.stat('~/python')```              |
| ```datetime.utime(path, times)``` | change the access time and modified time of the given <path>, if <times>=None then now()            |    ```datetime.utime('~/python')```              |
| ```datetime.walk(top, topdown=True, onerror=None, followlinks=False)```         | loop startswith the given <top> directory and return pathes and directory names  |    ```datetime.walk('~/python')```              |
| ```datetime.getenv(env, failvalue)``` | return the ```environment variable``` if successed or failvalue if failed   |    ```datetime.getenv('PYTHONPATH', 'Not Found')```              |

        |



## ```math```

```import math```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```re```

```import re```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```collections```

```import collections```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```tkinter```

```import tkinter```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |




## ```bisect```

```import bisect```

| Method                      | Description                                     | Usage                           |
| :-------------------------- | :---------------------------------------------- | :------------------------------ |
