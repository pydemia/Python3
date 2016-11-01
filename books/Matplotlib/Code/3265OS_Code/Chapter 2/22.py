import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-6, 6, 1024)
Y = numpy.sinc(X)

plot.plot(X, Y,
          linewidth = 3.,
          color = 'k',
          markersize = 9,
          markeredgewidth = 1.5,
          markerfacecolor = '.75',
          markeredgecolor = 'k',
          marker = 'o',
          markevery = 32)

plot.show()
