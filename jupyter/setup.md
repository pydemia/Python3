# Jupyter Setting

## Installation

## Configuration

## Add a Kernel

## Launch as a Daemon(Autostart)

Create a Service: 

```sh
sudo vi /etc/systemd/system/jupyter.service
```

```sh
[Unit]
Description=Jupyter Notebook

[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/home/bfortuner/anaconda3/bin/jupyter-notebook --config=/home/bfortuner/.jupyter/jupyter_notebook_config.py
User=bfortuner
Group=bfortuner
WorkingDirectory=/home/bfortuner/workplace
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then,
```sh
systemctl enable jupyter.service
systemctl daemon-reload
systemctl restart jupyter.service
```
