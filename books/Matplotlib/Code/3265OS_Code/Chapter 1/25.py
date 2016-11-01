import random
import matplotlib.pyplot as plot

count = 1000
X = [random.gauss(0, 1.) for i in range(count)]

plot.hist(X, bins = 20)
plot.show()
