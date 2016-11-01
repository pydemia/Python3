import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-6, 6, 1024)
Y1 = numpy.sinc(X)
Y2 = numpy.sinc(X) + 1

plot.plot(X, Y1, marker = 'o', color = '.75')
plot.plot(X, Y2, marker = 'o', color = 'k', markevery = 32)

plot.show()
