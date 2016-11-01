import numpy
import matplotlib.patches as patches
import matplotlib.pyplot as plot

ax = plot.axes(polar = True)

theta = numpy.linspace(0, 2 * numpy.pi, 8, endpoint = False)
radius = .25 + .75 * numpy.random.random(size = len(theta))
points = list(zip(theta, radius))

plot.gca().add_patch(patches.Polygon(points, color = '.75'))

plot.show()
