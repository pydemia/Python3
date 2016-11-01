import numpy
import matplotlib.pyplot as plot

M = numpy.random.standard_normal((1000, 2))
R = numpy.sum(M ** 2, axis = 1)

plot.scatter(M[:, 0], M[:, 1], c = 'w', marker = 's', s = 32. * R)
plot.show()
