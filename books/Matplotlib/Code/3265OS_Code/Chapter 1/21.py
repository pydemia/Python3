import random
import matplotlib.pyplot as plot

data = [random.gauss(0., 1.) for i in range(100)]

plot.boxplot(data)

plot.show()
