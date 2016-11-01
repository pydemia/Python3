import random
import matplotlib.pyplot as plot

name_list = ('Omar', 'Serguey', 'Max', 'Zhou', 'Abidin')
value_list = [random.randint(0, 99) for name in name_list]
pos_list = range(len(name_list))

plot.bar(pos_list, value_list, alpha = .5, color = '.25', align = 'center')

plot.xticks(pos_list, name_list)

plot.savefig('bar.png', transparent = True)
