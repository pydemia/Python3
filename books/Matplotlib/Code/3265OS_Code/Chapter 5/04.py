import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y) # 72, 96, 150, 300
plot.savefig('sinc.png', dpi = 100)
