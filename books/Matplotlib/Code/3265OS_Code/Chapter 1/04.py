import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 2 * numpy.pi, 100)
Ya = numpy.sin(X)
Yb = numpy.cos(X)

plot.plot(X, Ya)
plot.plot(X, Yb)
plot.show()
