import numpy
from matplotlib import pyplot as plot
from matplotlib.widgets import Slider



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
r = supershape_radius(phi, 1, 1, m_init, n1_init, n2_init, n3_init)

fig = plot.figure()
ax = fig.add_subplot(111, polar = True)

ax_m  = plot.axes([0.05, 0.05, 0.25, 0.025])
ax_n1 = plot.axes([0.05, 0.10, 0.25, 0.025])
ax_n2 = plot.axes([0.7, 0.05, 0.25, 0.025])
ax_n3 = plot.axes([0.7, 0.10, 0.25, 0.025])

slider_m  = Slider(ax_m,  'm',  1, 20, valinit = m_init)
slider_n1 = Slider(ax_n1, 'n1', .1, 10, valinit = n1_init)
slider_n2 = Slider(ax_n2, 'n2', .1, 20, valinit = n2_init)
slider_n3 = Slider(ax_n3, 'n3', .1, 20, valinit = n3_init)

lines, = ax.plot(phi, r, lw = 3.)

def update(val):
    lines.set_ydata(supershape_radius(phi, 1, 1, numpy.floor(slider_m.val), slider_n1.val, slider_n2.val, slider_n3.val))
    fig.canvas.draw_idle()

slider_n1.on_changed(update)
slider_n2.on_changed(update)
slider_n3.on_changed(update)
slider_m.on_changed(update)

plot.show()
