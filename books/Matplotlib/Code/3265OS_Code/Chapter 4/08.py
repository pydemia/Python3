import numpy
import matplotlib.pyplot as plot

T = numpy.linspace(0 , 2 * numpy.pi, 1024)

plot.axes(polar = True)
plot.plot(T, 1. + .25 * numpy.sin(16 * T), c = 'k')

plot.show()
