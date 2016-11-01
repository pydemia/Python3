import numpy
import matplotlib.pyplot as plot
import matplotlib.ticker as ticker

X = numpy.linspace(-15, 15, 1024)
Y = numpy.sinc(X)

ax = plot.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

#plot.grid(True, which='both')
plot.plot(X, Y, c = 'k')
plot.show()
