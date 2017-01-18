# Set up ```jupyterhub```

## On Server

On shell:
```sh
conda install -c conda-forge jupyterhub
jupyter notebook --generate-config
ipython
```

On ```ipython```
```python
In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password: 
Verify password: 
Out[2]: '<example>sha1:asdiugaasd8f9bas6da7b6a7sdbas78df7asdf86as9b8a<example>'
In [3]: exit
```

On ```jupyter_notebook_config.py```:
```python
c.NotebookApp.ip = '*'        # to use in public
c.NotebookApp.port = 8888     # set its port; can be modified
c.NotebookApp.password = '<example>sha1:asdiugaasd8f9bas6da7b6a7sdbas78df7asdf86as9b8a<example>'
```

## On Local

On browser:
```sh
{serverip}:8888
```
or
```sh
{serverip}:{jupyterport}
```


It's Done!
