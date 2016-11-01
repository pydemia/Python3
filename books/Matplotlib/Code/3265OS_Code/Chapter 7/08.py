import numpy
from matplotlib import cm
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

# Data generation
alpha = 1. / numpy.linspace(1, 8, 5)
t = numpy.linspace(0, 5, 16)
T, A = numpy.meshgrid(t, alpha)
data = numpy.exp(-T * A)

# Plotting
fig = plot.figure()
ax = fig.gca(projection = '3d')

cmap = cm.ScalarMappable(col.Normalize(0, len(alpha)), cm.gray)
for i, row in enumerate(data):
	ax.bar(4 * t, row, zs=i, zdir='y', alpha=0.8, color=cmap.to_rgba(i))

plot.show()
