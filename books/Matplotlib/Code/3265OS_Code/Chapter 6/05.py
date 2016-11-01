import numpy
from matplotlib import pyplot as plot
import matplotlib.cm as cm

n = 256
x = numpy.linspace(-3., 3., n)
y = numpy.linspace(-3., 3., n)
X, Y = numpy.meshgrid(x, y)

Z = X * numpy.sinc(X ** 2 + Y ** 2)

plot.pcolormesh(X, Y, Z, cmap = cm.gray)
plot.show()
