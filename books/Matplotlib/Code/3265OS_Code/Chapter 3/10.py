import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plot.plot(X, Y, c = 'k')

plot.grid(True, lw = 2, ls = '--', c = '.75')
plot.show()
