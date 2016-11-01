import numpy
import matplotlib.pyplot as plot

label_list = (
	b'Iris-setosa',
	b'Iris-versicolor',
	b'Iris-virginica',
)

def read_label(label):
	return label_list.index(label)

data = numpy.loadtxt('iris.data.txt',
                     delimiter = ',',
                     converters = { 4 : read_label })

color_set = ('.00', '.50', '.25')
color_list = [color_set[int(label)] for label in data[:,4]]

plot.scatter(data[:,0], data[:,1], color = color_list)
plot.show()

