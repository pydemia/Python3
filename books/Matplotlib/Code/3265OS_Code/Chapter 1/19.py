import numpy
import matplotlib.pyplot as plot

data = numpy.array([[5., 30., 45., 22.],
                    [5., 25., 50., 20.],
                    [1.,  2.,  1.,  1.]])

color_list = ['b', 'g', 'r']
X = range(data.shape[1])
for i, col in enumerate(color_list):
	plot.bar(X, data[i], bottom = numpy.sum(data[:i], axis = 0), color = col)

plot.show()
