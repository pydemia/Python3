import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plot.title(r'$f(x)=\frac{1}{4}(x+4)(x+1)(x-2)$')
plot.plot(X, Y, c = 'k')
plot.show()
