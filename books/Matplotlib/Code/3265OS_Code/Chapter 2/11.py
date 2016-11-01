import numpy
import matplotlib.pyplot as plot


def pdf(X, mu, sigma):
	a = 1. / (sigma * numpy.sqrt(2. * numpy.pi))
	b = -1. / (2. * sigma ** 2)
	return a * numpy.exp(b * (X - mu) ** 2)

X = numpy.linspace(-6, 6, 1024)

plot.plot(X, pdf(X, 0., 1.),   color = 'k', linestyle = 'solid')
plot.plot(X, pdf(X, 0.,  .5),  color = 'k', linestyle = 'dashed')
plot.plot(X, pdf(X, 0.,  .25), color = 'k', linestyle = 'dashdot')

plot.show()
