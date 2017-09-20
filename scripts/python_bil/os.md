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
