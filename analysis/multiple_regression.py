
import pandas as pd
from pandas import Series as sr
from pandas import DataFrame as df
import statsmodels.formula.api as sm

pd.read_csv()
adult = pd.read_csv('/media/dawkiny/M/BigData/Datasets/adult/adult.data', sep=',')
adult.columns
adult.head()

adult['net_capital'] = adult['capital_gain'] _ adult['capital_loss']
aa = adult.ix[:,('education_num', 'hours_per_week')].copy()
aa
xdat = aa['education_num']
ydat = aa['hours_per_week']
model = pd.ols(y=ydat, x=xdat)
model


aa = adult.ix[:,('education_num', 'net_capital')].copy()
aa
xdat = aa['education_num']
ydat = aa['net_capital']
model = pd.ols(y=ydat, x=xdat)
model


aa = adult.ix[:,('net_capital', 'hours_per_week')].copy()
aa
xdat = aa['net_capital']
ydat = aa['hours_per_week']
model = pd.ols(y=ydat, x=xdat)
model


res = sm.ols(formula = 'net_capital ~ hours_per_week + race + sex', data = adult).fit()
res.summary()
