import numpy
import matplotlib.pyplot as plot

A = numpy.random.standard_normal((100, 2))
A += numpy.array((-1, -1))

B = numpy.random.standard_normal((100, 2))
B += numpy.array((1, 1))

plot.scatter(B[:,0], B[:,1], c = 'k', s = 100.)
plot.scatter(A[:,0], A[:,1], c = 'w', s = 25.)

plot.show()
