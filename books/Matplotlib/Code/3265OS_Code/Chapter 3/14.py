import numpy
import matplotlib.pyplot as plot

theta = numpy.linspace(0, 2 * numpy.pi, 8)
points = numpy.vstack((numpy.cos(theta), numpy.sin(theta))).transpose()

plot.gca().add_patch(plot.Polygon(points, color = '.75'))

plot.grid(True)
plot.axis('scaled')
plot.show()
