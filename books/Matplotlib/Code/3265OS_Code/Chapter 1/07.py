import numpy
import matplotlib.pyplot as plot

data = numpy.loadtxt('sample.txt')

plot.plot(data[:,0], data[:,1])
plot.show()
