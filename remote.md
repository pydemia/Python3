Here are the steps I took to be able to debug on Windows a program running on Linux.

Open Debug Perspective in Eclipse(Windows), and start PyDev Server
On linux run ```pip install pydevd```
Create a file on both windows and linux with code below
Run the created script on Linux
When code reaches pydevd.settrace statement it will connect to Eclipse running on Windows, and Eclipse will ask you where it can find the code, point it to where you've stored it on windows.
Now you can step through the code, check variable values and etc...

```python
#!/usr/bin/env python
import os
import pydevd
pydevd.settrace("EclipseIDE_HOSTNAME", port=5678)

a = 1
b = 2
c = a + b

s = 'hello world'
print s
```
