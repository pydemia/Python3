import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-3, 2, 200)
Y = X ** 2 - 2 * X + 1.

plot.plot(X, Y)
plot.show()
