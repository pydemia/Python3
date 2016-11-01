import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(1, 10, 1024)

plot.yscale('log', basey=2)

plot.plot(X, X, c = 'k', lw = 2., label = r'$f(x)=x$')
plot.plot(X, 10 ** X, c = '.75', ls = '--', lw = 2., label = r'$f(x)=e^x$')
plot.plot(X, numpy.log(X), c = '.75', lw = 2., label = r'$f(x)=\log(x)$')

plot.legend()
plot.show()
