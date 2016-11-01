import numpy
import matplotlib.cm as cm
import matplotlib.pyplot as plot

N = 256
angle  = numpy.linspace(0, 8 * 2 * numpy.pi, N)
radius = numpy.linspace(.5, 1., N)

X = radius * numpy.cos(angle)
Y = radius * numpy.sin(angle)

#plot.scatter(X, Y, c = angle, cmap = cm.hsv)
plot.scatter(X, Y, c = angle, cmap = cm.PuOr)
plot.show()
