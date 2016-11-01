import numpy
import matplotlib.ticker as ticker
import matplotlib.pyplot as plot

name_list = ('Omar', 'Serguey', 'Max', 'Zhou', 'Abidin')
value_list = numpy.random.randint(0, 99, size = len(name_list))
pos_list = numpy.arange(len(name_list))

ax = plot.axes()
ax.xaxis.set_major_locator(ticker.FixedLocator((pos_list)))
ax.xaxis.set_major_formatter(ticker.FixedFormatter((name_list)))

plot.bar(pos_list, value_list, color = '.75', align = 'center')

plot.show()
