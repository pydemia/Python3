import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

angle = numpy.linspace(0, 2 * numpy.pi, 64)
theta, phi = numpy.meshgrid(angle, angle)

r, R = .25, 1.
X = (R + r * numpy.cos(phi)) * numpy.cos(theta)
Y = (R + r * numpy.cos(phi)) * numpy.sin(theta)
Z = r * numpy.sin(phi)

fig = plot.figure()
ax = fig.gca(projection = '3d')

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
#ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, linewidth = 0, antialiased = False, cmap = plot.get_cmap('jet'))
#ax.pbaspect = [6., 6., 1]
#ax.plot_surface(X, Y, Z, color = 'w', rstride = 1, cstride = 1)
ax.plot_wireframe(X, Y, Z, color = 'k')


plot.show()

