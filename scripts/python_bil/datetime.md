
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
