import numpy
import matplotlib.path as mpath
from matplotlib import pyplot as plot

shape_description = [
	( 1.,  2., mpath.Path.MOVETO),
	( 1.,  1., mpath.Path.LINETO),
	( 2.,  1., mpath.Path.LINETO),
	( 2., -1., mpath.Path.LINETO),
	( 1., -1., mpath.Path.LINETO),
  ( 1., -2., mpath.Path.LINETO),
	(-1., -2., mpath.Path.LINETO),
	(-1., -1., mpath.Path.LINETO),
	(-2., -1., mpath.Path.LINETO),
	(-2.,  1., mpath.Path.LINETO),
	(-1.,  1., mpath.Path.LINETO),
	(-1.,  2., mpath.Path.LINETO),
	( 0.,  0., mpath.Path.CLOSEPOLY),
]

u, v, codes = zip(*shape_description)
my_marker = mpath.Path(numpy.asarray((u, v)).T, codes)

data = numpy.random.rand(8, 8)
plot.scatter(data[:,0], data[:, 1], c = '.75', marker = my_marker, s = 64)
plot.show()
