import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 2 * numpy.pi, 100)
Y = numpy.sin(X)

plot.plot(X, Y)
plot.show()
