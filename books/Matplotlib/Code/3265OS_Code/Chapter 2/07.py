import random
import matplotlib.pyplot as plot

values = [random.random() for i in range(8)]

color_set = ['.00', '.25', '.50', '.75']
plot.pie(values, colors = color_set)
plot.show()
