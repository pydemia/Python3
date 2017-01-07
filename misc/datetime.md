# Datetime Regular Expression

```python


'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
#-------------------------
'The day is 11, the month is March.'
```

|Format|Description|
|:-----|:----------|
| %Y | Year(4 digits) |
| %y | Year(2 digits) |
| %m | Month(2 digits) |
| %B | Month(str) |
| %b | Month-alias(str) |
| %d | Day(2 digits) |
| %H | Hour(24h) |
| %I | Hour(12h) |
| %p | AM, PM |
| %M | Minute(2 digits) |
| %S | Second(2 digits) |
| %w | Weekday(Int)[0:Sun] |
| %A | Weekday(str)[0:Sun] |
| %a | Weekday-alias(str)[0:Sun] |
| %U | Week(startswith Sun) |
| %W | Week(startswith Mon) |
| %F | %Y-%m-%d |
| %D | %m/%d/%y |
| %X | Locale TimeFormat (%I:%M:%s %p) |
| %x | Locale DateFormat (%m/%d/%Y) |


