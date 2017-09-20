
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

