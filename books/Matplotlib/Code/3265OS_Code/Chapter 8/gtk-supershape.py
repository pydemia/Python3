from gi.repository import Gtk

import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg



def supershape_radius(phi, a, b, m, n1, n2, n3):
	theta = .25 * m * phi
	cos = numpy.fabs(numpy.cos(theta) / a) ** n2
	sin = numpy.fabs(numpy.sin(theta) / b) ** n3
	r = (cos + sin) ** (-1. / n1)
	r /= numpy.max(r)
	return r


phi = numpy.linspace(0, 2 * numpy.pi, 1024)
m_init = 3
n1_init = 2
n2_init = 18
n3_init = 18


fig = Figure((6, 6), dpi = 80)
ax = fig.add_subplot(111, polar = True)

r = supershape_radius(phi, 1, 1, m_init, n1_init, n2_init, n3_init)
lines, = ax.plot(phi, r, lw = 3.)


win = Gtk.Window()
win.connect('delete-event', Gtk.main_quit)
win.set_title('SuperShape')

canvas = FigureCanvasGTK3Agg(fig)
w, h = fig.get_size_inches()
dpi_res = fig.get_dpi()
w, h = int(numpy.ceil(w * dpi_res)), int(numpy.ceil(h * dpi_res))
canvas.set_size_request(w, h)
win.add(canvas)

win.show_all()
Gtk.main()
