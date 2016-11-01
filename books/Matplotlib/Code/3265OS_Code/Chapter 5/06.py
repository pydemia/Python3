import numpy
from matplotlib import pyplot as plot

X = numpy.linspace(-10, 10, 1024)
Y = numpy.sinc(X)

fig = plot.figure(figsize = (33.11, 46.81))
plot.plot(X, Y)
plot.savefig('sinc.pdf')
