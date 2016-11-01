import numpy
import matplotlib as mpl
from matplotlib import pyplot as plot

mpl.rc('lines', linewidth = 2.)
mpl.rc('axes', facecolor = 'k', edgecolor = 'w')
mpl.rc('xtick', color = 'w')
mpl.rc('ytick', color = 'w')
mpl.rc('text', color = 'w')
mpl.rc('figure', facecolor = 'k', edgecolor ='w')
mpl.rc('axes', color_cycle = ('w', '.5', '.75'))
mpl.rc('savefig', facecolor = 'k', edgecolor = 'w')
X = numpy.linspace(0, 7, 1024)

plot.plot(X, numpy.sin(X))
plot.plot(X, numpy.cos(X))
plot.show()
