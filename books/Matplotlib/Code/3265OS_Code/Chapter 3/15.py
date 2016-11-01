import numpy
import matplotlib.pyplot as plot

theta = numpy.linspace(0, 2 * numpy.pi, 6)
points = list(zip(numpy.cos(theta), numpy.sin(theta)))

plot.gca().add_patch(plot.Circle((0, 0), radius = 1., color = '.75'))
plot.gca().add_patch(plot.Polygon(points, closed=None, fill=None, lw = 3., ls = 'dashed', edgecolor = 'k'))

plot.grid(True)
plot.axis('scaled')
plot.show()
