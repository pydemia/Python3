import numpy, datetime
import matplotlib.pyplot as plot
import matplotlib.dates as dates
import matplotlib.ticker as ticker

start_date = datetime.datetime(1998, 1, 1)

def make_label(value, pos):
	time = start_date + datetime.timedelta(days = 365 * value)
	return time.strftime('%b %y')

ax = plot.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

X = numpy.linspace(0, 1, 256)
plot.plot(X, numpy.exp(-10 * X), c = 'k')
plot.plot(X, numpy.exp(-5 * X), c = 'k', ls = '--')

labels = ax.get_xticklabels()
plot.setp(labels, rotation = 30.)

plot.show()
