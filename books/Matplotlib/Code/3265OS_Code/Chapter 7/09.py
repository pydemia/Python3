import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

# Data generation
alpha = numpy.linspace(1, 8, 5)
t = numpy.linspace(0, 5, 16)
T, A = numpy.meshgrid(t, alpha)
data = numpy.exp(-T * (1. / A))

# Plotting
fig = plot.figure()
ax = fig.gca(projection = '3d')

Xi = T.flatten()
Yi = A.flatten()
Zi = numpy.zeros(data.size)

dx = .25 * numpy.ones(data.size)
dy = .25 * numpy.ones(data.size)
dz = data.flatten()

ax.set_xlabel('T')
ax.set_ylabel('Alpha')
ax.bar3d(Xi, Yi, Zi, dx, dy, dz, color = 'w')

plot.show()
