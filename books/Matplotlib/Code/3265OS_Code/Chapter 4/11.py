import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-6, 6, 1024)
plot.plot(X, numpy.sinc(X))
plot.xticks([])
plot.yticks([])
plot.show()
