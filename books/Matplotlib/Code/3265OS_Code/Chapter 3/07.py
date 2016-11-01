import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

box = {
	'facecolor' : '.75',
	'edgecolor' : 'k',
  'boxstyle'  : 'round'
}

plot.text(-0.5, -0.20, 'Brackmard minimum', bbox = box)

plot.plot(X, Y, c = 'k')
plot.show()
