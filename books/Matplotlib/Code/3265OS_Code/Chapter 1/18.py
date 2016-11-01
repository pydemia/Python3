import numpy
import matplotlib.pyplot as plot

data = numpy.array([[5., 30., 45., 22.],
                    [5., 25., 50., 20.],
                    [1.,  2.,  1.,  1.]])

color_list = ['b', 'g', 'r']

X = numpy.arange(data.shape[1])
for i in range(data.shape[0]):
	S = numpy.sum(data[:i], axis = 0)
	plot.bar(X, data[i], bottom = S, color = color_list[i % len(color_list)])

plot.show()
