import numpy
import matplotlib.pyplot as plot


def pdf(X, mu, sigma):
	a = 1. / (sigma * numpy.sqrt(2. * numpy.pi))
	b = -1. / (2. * sigma ** 2)
	return a * numpy.exp(b * (X - mu) ** 2)

X = numpy.linspace(-6, 6, 1024)

for i in range(5):
	samples = numpy.random.standard_normal(50)
	mu, sigma = numpy.mean(samples), numpy.std(samples)
	plot.plot(X, pdf(X, mu, sigma), color = '.75')

plot.plot(X, pdf(X, 0., 1.), color = 'k')

plot.show()
