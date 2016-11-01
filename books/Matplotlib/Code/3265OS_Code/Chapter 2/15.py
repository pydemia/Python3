import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 6, 1024)
Y1 = numpy.sin(X)
Y2 = numpy.cos(2 * X)

plot.fill_between(X, Y1, Y2, color = '.75')

plot.show()
