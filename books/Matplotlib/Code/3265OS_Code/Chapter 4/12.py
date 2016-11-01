import numpy
from matplotlib import pyplot as plot

T = numpy.linspace(-numpy.pi, numpy.pi, 1024)

fig, (ax0, ax1) = plot.subplots(ncols=2)

ax0.plot(numpy.sin(2 * T), numpy.cos(0.5 * T), c= 'k')
ax1.plot(numpy.cos(3 * T), numpy.sin(T), c= 'k')

plot.show()
