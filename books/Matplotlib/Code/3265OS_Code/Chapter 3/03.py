import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plot.title('Power curve for airfoil KV873')
plot.xlabel('Air speed')
plot.ylabel('Total drag')

plot.plot(X, Y, c = 'k')
plot.show()
