import numpy, sympy
from sympy.abc import x, y
from matplotlib import pyplot as plot
import matplotlib.patches as patches
import matplotlib.cm as cm

def cylinder_stream_function(U = 1, R = 1):
	r = sympy.sqrt(x ** 2 + y ** 2)
	theta = sympy.atan2(y, x)
	return U * (r - R ** 2 / r) * sympy.sin(theta)

def velocity_field(psi):
	u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
	v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
	return u, v

psi = cylinder_stream_function()
U_func, V_func = velocity_field(psi)

xmin, xmax, ymin, ymax = -3, 3, -3, 3
Y, X = numpy.ogrid[ymin:ymax:128j, xmin:xmax:128j]
U, V = U_func(X, Y), V_func(X, Y)

M = (X ** 2 + Y ** 2) < 1.
U = numpy.ma.masked_array(U, mask = M)
V = numpy.ma.masked_array(V, mask = M)

shape = patches.Circle((0, 0), radius = 1., lw = 2., fc = 'w', ec = 'k', zorder = 0)
plot.gca().add_patch(shape)

plot.streamplot(X, Y, U, V, color = U ** 2 + V ** 2, cmap = cm.binary)

plot.axes().set_aspect('equal')
plot.show()
