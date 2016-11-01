import numpy
from matplotlib import pyplot as plot

def get_radius(T, params):
	m, n_1, n_2, n_3 = params
	U = (m * T) / 4
	return (numpy.fabs(numpy.cos(U)) ** n_2 + numpy.fabs(numpy.sin(U)) ** n_3) ** (-1. / n_1)

grid_size = (3, 4)
T = numpy.linspace(0, 2 * numpy.pi, 1024)

for i in range(grid_size[0]):
	for j in range(grid_size[1]):
		params = numpy.random.random_integers(1, 20, size = 4)
		R = get_radius(T, params)

		axes = plot.subplot2grid(grid_size, (i, j), rowspan=1, colspan=1)
		axes.get_xaxis().set_visible(False)
		axes.get_yaxis().set_visible(False)
		plot.plot(R * numpy.cos(T), R * numpy.sin(T), c = 'k')

		plot.title('%d, %d, %d, %d' % tuple(params), fontsize = 'small')

plot.tight_layout()
plot.show()
