# pip install
```sh
pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org [PackageName]
```

# conda install
```sh
conda config --set ssl_verify false
```

# custom_modification
1. download ```ibm_db.2.0.7.tar.gz``` from ```https://pypi.python.org/pypi/ibm_db```.   
2. edit ```setup.py```; change url(startswith ```https://``` to ```http://```) manually.  
3. change directory to ```ibm_db.2.0.7.tar.gz```.  
4. ```sh
pip install ibm_db_2.0.7.tar.gz
```
 
