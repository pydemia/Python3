import numpy
import matplotlib.pyplot as plot
import matplotlib.ticker as ticker

def make_label(value, pos):
	return '%0.1f%%' % (100. * value)

ax = plot.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

X = numpy.linspace(0, 1, 256)
plot.plot(X, numpy.exp(-10 * X), c = 'k')
plot.plot(X, numpy.exp(-5 * X), c = 'k', ls = '--')

plot.show()
