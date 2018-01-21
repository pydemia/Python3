
## `argparse`

```py
import argparse
```

```py
parser = argparse.ArgumentParser(description='This is a Sample')
parser.add_argument('--method', '-I',
                    dest='method'
                    action="store_true",
                    type=str,
                    choices=['mean', 'var'],
                    default='mean',
                    required=True,
                    help="echo the string you use here")
parser.parse_args()

method = parser.method
```
