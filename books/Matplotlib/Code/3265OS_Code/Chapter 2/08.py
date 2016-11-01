import random
import matplotlib.pyplot as plot

values = [random.gauss(0., 1.) for i in range(100)]

b = plot.boxplot(values)
print b.keys()
for name, line_list in b.iteritems():
	for line in line_list:
		line.set_color('k')

plot.show()
