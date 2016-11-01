import numpy
import matplotlib.pyplot as plot

name_list = ('Omar', 'Serguey', 'Max', 'Zhou', 'Abidin')
value_list = numpy.random.randint(0, 99, size = len(name_list))
pos_list = numpy.arange(len(name_list))

plot.bar(pos_list, value_list, color = '.75', align = 'center')

plot.xticks(pos_list, name_list)

plot.show()
