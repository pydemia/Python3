import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-100, 100, 4096)

plot.xscale('symlog', linthreshx=6.)

plot.plot(X, numpy.sinc(X), c = 'k')
plot.show()
