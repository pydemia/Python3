import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plot.text(-0.5, -0.25, 'Brackmard minimum')

plot.plot(X, Y, c = 'k')
plot.show()
