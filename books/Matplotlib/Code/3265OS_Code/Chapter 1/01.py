import matplotlib.pyplot as plot

X = range(100) 
Y = [x ** 2 for x in X]

plot.plot(X, Y)
plot.show()
