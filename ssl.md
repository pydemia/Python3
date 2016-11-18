# SSL Certification

---
## Bypass cert

### ```pip```
```sh
pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org [PackageName]
```

### ```conda```
```sh
conda config --set ssl_verify false
```


---
## Use cert

### ```pip```
```sh
pip --cert [sslproxy.crt] [PackageName]
```

### ```conda```
```sh
conda config --set ssl_verify [sslproxy.crt]
```

---
## custom_configuration
1. download ```ibm_db.2.0.7.tar.gz``` from ```https://pypi.python.org/pypi/ibm_db```.   
2. edit ```setup.py```; change url(startswith ```https://``` to ```http://```) manually.  
3. change directory to ```ibm_db.2.0.7.tar.gz```.  
4. ```pip install ibm_db_2.0.7.tar.gz``` 

