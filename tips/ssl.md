# SSL

```bash
# openssl
openssl version -a
OPENSSLDIR: "/home/kube/miniconda3/envs/<conda-env-name>/ssl"

export SSL_CERT_DIR="${HOME}/.ssl"                                              
export SSL_CERT_FILE="${HOME}/.ssl/SK_SSL.crt"                                  

# requests
export REQUESTS_CA_BUNDLE="${HOME}/.ssl/SK_SSL.crt"                             

# curl
export CURL_CA_BUNDLE="${HOME}/.ssl/SK_SSL.crt"   
```


## Verify SSL in code

* `urllib3`:

```py
import ssl

if os.getenv("SSL_CERT_FILE"):
    ssl._create_default_https_context = ssl.create_default_context(
        capath=,
    )
else:
    ssl._create_default_https_context = ssl._create_unverified_context

```

