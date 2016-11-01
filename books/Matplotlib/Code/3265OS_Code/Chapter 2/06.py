import random
import matplotlib.pyplot as plot

values = [random.randint(0, 99) for i in range(50)]

color_set = ['.00', '.25', '.50', '.75']
color_list = [color_set[(len(color_set) * val) // 100] for val in values]

plot.bar(range(len(values)), values, color = color_list)
plot.show()
