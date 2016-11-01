import numpy
import matplotlib.pyplot as plot

data, label_list = [], []
for line in open('iris.data.txt'):
	tokens = line.split(',')
	data.append([float(s) for s in tokens[:-1]])
	label_list.append(tokens[-1])

data_map = { label : [] for label in set(label_list) }
for point, label in zip(data, label_list):
	data_map[label].append(point)
 
marker_set = ['^', 'x', '.']

for marker, (label, subset) in zip(marker_set, data_map.iteritems()):
	data = numpy.asarray(subset)
	plot.scatter(data[:,0], data[:,1], color = 'k', marker = marker)

plot.show()
