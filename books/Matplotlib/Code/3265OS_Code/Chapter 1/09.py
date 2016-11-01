import random
import matplotlib.pyplot as plot

count = 1024
X = [random.random() for i in range(count)]
Y = [random.random() for i in range(count)]

plot.scatter(X, Y)
plot.show()

