import numpy
import matplotlib.pyplot as plot

def plot_slope(X, Y):
	Xs = X[1:] - X[:-1]
	Ys = Y[1:] - Y[:-1]
	plot.plot(X[1:], Ys / Xs)

X = numpy.linspace(-3, 3, 100)
Y = numpy.exp(-X ** 2)

plot.plot(X, Y)
plot_slope(X, Y)
plot.show()
