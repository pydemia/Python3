import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

# Dataset generation
a, b, c = 10., 28., 8. / 3.
def lorenz_map(X, dt = 1e-2):
	X_dt = numpy.array([a * (X[1] - X[0]),
	                    X[0] * (b - X[2]) - X[1],
	                    X[0] * X[1] - c * X[2]])
	return X + dt * X_dt

points = numpy.zeros((2000, 3))
X = numpy.array([.1, .0, .0])
for i in range(points.shape[0]):
	points[i], X = X, lorenz_map(X)

# Plotting
fig = plot.figure()
ax = fig.gca(projection = '3d')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))

'''
ax.scatter(points[:, 0], points[:, 1],  points[:, 2],
           marker = 's',
           edgecolor = '.5',
           facecolor = '.5')
'''
ax.scatter(points[:, 0], points[:, 1],  points[:, 2],
           zdir = 'z',
           c = '.5')
plot.show()
