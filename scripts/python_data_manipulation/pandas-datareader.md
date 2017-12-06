# Pandas-datareader

## Installation
```sh
pip install pandas-datareader
```

```py
import pandas_datareader as pdr
```


Note : To Fix Google Finance 1-year limit problem

```py
from pandas_datareader.google.daily import GoogleDailyReader

class FixedGoogleDailyReader(GoogleDailyReader):
    @property
    def url(self):
        # 'http://www.google.com/finance/historical' -> 'http://finance.google.com/finance/historical'
        return 'http://finance.google.com/finance/historical'

```

