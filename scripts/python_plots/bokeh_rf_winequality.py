#/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Created on Mon Oct 30 16:58:37 2017

@author: Young Ju Kim
'''

# %% Import for Analysis

import numpy as np
import scipy as sp
import scipy.stats as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import unipy as up
import unipy.dataset.api as dm

# %% Import for Bokeh

from bokeh.io import curdoc
from bokeh.layouts import (row, column, widgetbox, layout)
from bokeh.models import (ColumnDataSource, DataRange1d, Plot,
                         LinearAxis, Grid, Range1d)
from bokeh.models.glyphs import VBar
from bokeh.models.widgets import (Slider, TextInput, Paragraph,
                                  DataTable, TableColumn, Button)
from bokeh.plotting import figure

# %% Random Forest

dm.init()
data = dm.load('winequality_red')
dataX = data.iloc[:, :-1]
dataY = data.iloc[:, -1]  # data.iloc[:,[ -1]]

trainX, testX, trainY, testY = train_test_split(dataX, dataY,
                                                test_size=.4,
                                                shuffle=True,
                                                random_state=123)


model = RandomForestRegressor()
model.fit(trainX, trainY)

df_importance = pd.DataFrame({'feature': trainX.columns,
                              'score': model.feature_importances_})

r_sqr_str = 'R-Square : %.4f' % model.score(testX, testY)

x_values = dataX.describe()
y_values = dataY.describe()
model.predict(x_values.loc[['mean'], :])[0]

# %%


rsq = Paragraph(text=r_sqr_str, width=100, height=10)

# Importance Table
imp_outputDF = df_importance.sort_values(by='score', ascending=False)
imp_resultDF = ColumnDataSource(imp_outputDF)
imp_columns = [TableColumn(field=col, title=col)\
               for col in imp_outputDF.columns]
imp_data_table = DataTable(source=imp_resultDF,
                           columns=imp_columns, width=300, height=400)

# Setup Widgets
text = TextInput(title='title', value='Enter the name of Y')
SliderList_x = [Slider(title=col,
                       value=x_values.loc['mean', col],
                       start=x_values.loc['min', col],
                       end=x_values.loc['max', col],
                       step=(x_values.loc['max', col] - x_values.loc['min', col]) / 100,
                       orientation='vertical',
                       width=100,
                       height=400) for col in x_values.columns]

# Get the current slider values
presentDF = pd.DataFrame.from_dict({val.title: val.value\
                                    for val in SliderList_x}, orient='index').T
pred = model.predict(presentDF)
source = ColumnDataSource(data=dict(x=[.5], y=pred))

y_name = Paragraph(text='Wine Quality', width=100, height=10)

# Setup a plot
plot = figure(plot_height=450, plot_width=70, title=str('%.3f' % pred[0]),
              tools='crosshair, pan, reset, save, wheel_zoom')
plot.vbar_stack(['y'], x=.5, width=.3, source=source, color='firebrick')
plot.x_range = Range1d(0, 1)
plot.y_range = Range1d(y_values['min'], y_values['max'])

def update_data(attrname, old, new):

    # Get the current silder values
    presentDF = pd.DataFrame.from_dict({val.title: val.value\
                                        for val in SliderList_x},
                                       orient='index').T
    pred = model.predict(presentDF)
    console_x = presentDF.T
    console_x.columns = ['score']
    print(console_x)
    print(pred)
    source.data = dict(x=[.5], y=pred)
    plot.title.text = str('%.3f' % pred[0])


for w in SliderList_x:
    w.on_change('value', update_data)


def update_yname(attrname, old, new):
    y_name.text = text.value

text.on_change('value', update_yname)


# Setup UI Frame
lo = layout([[text, rsq],
            SliderList_x + [[y_name] + [plot]],
            [imp_data_table],
            ], sizing_mode='fixed')

curdoc().add_root(column(lo, height=100, width=100))
curdoc().title = 'Prototype : Wine Quality Simulator'

