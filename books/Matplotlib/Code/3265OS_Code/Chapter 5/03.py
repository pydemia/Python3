import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y)
plot.savefig('sinc.png', bbox_inches = 'tight')
