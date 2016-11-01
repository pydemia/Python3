import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plot.annotate('Brackmard minimum',
              ha = 'center', va = 'bottom',
              xytext = (-1.5, 3.),
              xy = (0.75, -2.7),
              arrowprops = { 'facecolor' : 'k', 'shrink' : 0.05 })

plot.plot(X, Y, c = 'k')
plot.show()
