import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox, layout
from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid, Range1d
from bokeh.models.widgets import Slider, TextInput, Paragraph, DataTable, TableColumn, Button
from bokeh.plotting import figure

import unipy.dataset.api as dm

dm.init()
df = dm.load('winequality_red')
X_train, y_train = df.drop(['quality'], axis=1).iloc[:30,:], df['quality'][:30]
X_test, y_test = df.drop(['quality'], axis=1).iloc[30:40,:], df['quality'][30:40]
model = RandomForestRegressor(n_estimators=200, random_state=0, max_features=None)
fit = model.fit(X_train, y_train)
pred = fit.predict(X_test)

x_values = X_train.apply([np.mean, np.max, np.min])

y_values = y_train.apply([np.mean, np.max, np.min])


r2_str = 'R2 : %.7f' % r2_score(y_test, pred)
imp = pd.DataFrame(fit.feature_importances_, columns=['score'])



rsq = Paragraph(text=r2_str, width=100, height=10)

outputDF = pd.DataFrame(columns=X_train.columns)
resultDF = ColumnDataSource(outputDF)
columns = [TableColumn(field=col, title=col) for col in outputDF.columns]
data_table = DataTable(source=resultDF, columns=columns, width=1000, height=400)

imp_outputDF = imp.sort_values(by='score', ascending=False)
imp_resultDF = ColumnDataSource(imp_outputDF)
imp_columns = [TableColumn(field=col, title=col) for col in imp_outputDF.columns]
imp_data_table = DataTable(source=imp_resultDF, columns=imp_columns, width=300, height=400)

text = TextInput(title='title', value='my indicator')
SliderList_x = [Slider(title=col,
                       value=x_values.loc['mean', col],
                       start=x_values.loc['amin', col],
                       end=x_values.loc['amax', col],
                       step=.01,
                       orientation='vertical',
                       width=100,
                       height=400) for col in x_values.columns]

x = [1]

presentDF = pd.DataFrame.from_dict({val.title: val.value for val in SliderList_x}, orient='index').T
pred = fit.predict(presentDF)
source = ColumnDataSource(data=dict(x=x, y=pred))

y_indicator = Paragraph(text=str('%f' % pred[0]), width=100, height=10)

plot = figure(plot_height=450, plot_width=70, title='',
              tools='crosshair, pan, reset, save, wheel_zoom')
plot.vbar_stack(['y'], x=.5, width=.5, source=source, color='firebrick')
plot.x_range = Range1d(0, 1)
plot.y_range = Range1d(y_values['amin'], y_values['amax'])

   
def update_data(attrname, old, new):

    presentDF = pd.DataFrame.from_dict({val.title: val.value for val in SliderList_x}, orient='index').T
    #presentDF['SUM_PT'] = presentDF.sum(axis=1)
    pred = fit.predict(presentDF)
    source.data = dict(x=x, y=pred)
    y_indicator.text = str('%f' % pred[0])

 
for w in SliderList_x:
    w.on_change('value', update_data)

lo = layout([[text, rsq],
            SliderList_x + [[y_indicator] + [plot]] + [imp_data_table],
            [data_table],
            ], sizing_mode='fixed')

curdoc().add_root(column(lo, height=100, width=100))
curdoc().title = 'Simulator'


