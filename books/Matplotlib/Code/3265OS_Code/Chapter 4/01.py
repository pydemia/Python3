import numpy
from matplotlib import pyplot as plot

T = numpy.linspace(-numpy.pi, numpy.pi, 1024)

grid_size = (4, 2)

plot.subplot2grid(grid_size, (0, 0), rowspan=3, colspan=1)
plot.plot(numpy.sin(2 * T), numpy.cos(0.5 * T), c= 'k')

plot.subplot2grid(grid_size, (0, 1), rowspan=3, colspan=1)
plot.plot(numpy.cos(3 * T), numpy.sin(T), c= 'k')

plot.subplot2grid(grid_size, (3, 0), rowspan=1, colspan=3)
plot.plot(numpy.cos(5 * T), numpy.sin(7 * T), c= 'k')

plot.tight_layout()
plot.show()
