import numpy
from matplotlib import pyplot as plot


X = numpy.linspace(-6, 6, 1024)
plot.plot(X, numpy.sinc(X), c = 'k')

a = plot.axes([.6, .6, .25, .25])
X = numpy.linspace(-3, 3, 1024)
a.plot(X, numpy.sinc(X), c = 'k')
plot.setp(a)

plot.show()
