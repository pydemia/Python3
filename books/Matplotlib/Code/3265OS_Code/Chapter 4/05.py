import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-6, 6, 1024)
Y1, Y2 = numpy.sinc(X), numpy.cos(X)

fig = plot.figure(figsize=(10.24, 2.56))

#plot.ylim(-0.5 * numpy.pi, 0.5 * numpy.pi)

plot.plot(X, Y1, c='k', lw = 3.)
plot.plot(X, Y2, c='.75', lw = 3.)
plot.show()

