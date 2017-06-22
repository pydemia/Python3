# Input & Output

## ```open()```


```open()``` returns a file object

```python
open(filename, mode)
```

```python
aFile = open('tempfile', 'w')
```

| MODE      | OPTION                 |
| :-------: | :--------------------- |
| ```'r'``` | read only(default)     |
| ```'w'``` | write only, truncating the file first             |
| ```'x'``` | write only             |
| ```'a'``` | append                 |
| ```'b'``` | binary mode                 |
| ```'t'``` | text mode(default)                 |
| ```'r+'```| read, write            |
| ```'w+b'``` | opens and truncates the file to 0 bytes |
| ```'r+b'``` | opens the file without truncation |


## Methods of the File Objects

#### ```read()```

```python
f.read()
'This is the entire file.\n'
f.read()
''
```

#### ```readline()```

```python
f.readline()
'This is the first line of the file.\n'
f.readline()
'Second line of the file\n'
f.readline()
''
```


```python
for line in f:
...     print(line, end='')

This is the first line of the file.
Second line of the file
```

#### ```write()```

#### ```seek()```

#### ```close()```

#### ```closed```

Usage:
```python
with open('tempfile') as aFile:
    print(aFile.readline(), end='\n')

with open('output.txt', 'w') as aFile:
    aFile.write('It\'s done.')
```


## ```json```


## ```pickle```


## ```dill```
```python
import dill                            #pip install dill --user

filename= 'globalsave.pkl'
dill.dump_session(filename)

# and to load the session again:
dill.load_session(filename)
```


## ```readline```

Dump Python Interactive Session to a File

```python
import readline
readline.write_history_file('my_history.py')
```
