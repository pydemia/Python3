import numpy
import matplotlib.pyplot as plot

data = numpy.random.standard_normal((100, 2))

plot.scatter(data[:,0], data[:,1], color = '1.0', edgecolor='0.0')
plot.show()
