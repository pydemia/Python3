import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 6, 1024)
Y1 = numpy.sin(X)
Y2 = numpy.cos(X)

plot.xlabel('X')
plot.xlabel('Y')

plot.plot(X, Y1, c = 'k',             lw = 3., label = 'sin(X)')
plot.plot(X, Y2, c = '.5', ls = '--', lw = 3., label = 'cos(X)')

plot.legend()
plot.show()
