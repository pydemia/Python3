import numpy
import matplotlib.pyplot as plot

T = numpy.linspace(0, 2 * numpy.pi, 1024)

plot.plot(2. * numpy.cos(T), numpy.sin(T), c = 'k', lw = 3.)
#plot.axes().set_aspect('equal')

plot.show()
