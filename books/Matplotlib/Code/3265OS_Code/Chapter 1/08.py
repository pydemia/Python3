import numpy
import matplotlib.pyplot as plot

data = numpy.loadtxt('sample.txt')

for column in data.T:
	plot.plot(data[:,0], column)

plot.show()

