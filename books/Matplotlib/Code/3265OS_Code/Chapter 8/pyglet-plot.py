import pyglet, math, numpy, StringIO

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg



def render_figure(fig):
	w, h = fig.get_size_inches()
	dpi_res = fig.get_dpi()
	w, h = int(math.ceil(w * dpi_res)), int(math.ceil(h * dpi_res))

	canvas = FigureCanvasAgg(fig)
	pic_data = StringIO.StringIO()
	canvas.print_raw(pic_data, dpi = dpi_res)
	return pyglet.image.ImageData(w, h, 'RGBA', pic_data.getvalue(), -4 * w)



def draw_figure():
	X = numpy.linspace(-6, 6, 1024)
	Y = numpy.sinc(X)

	fig = Figure()
	ax = fig.add_subplot(111)
	ax.plot(X, Y, lw = 2, color = 'k')
	
	return fig



image = render_figure(draw_figure())
window = pyglet.window.Window(image.width, image.height)

@window.event
def on_draw():
	window.clear()
	image.blit(0, 0)

pyglet.app.run()
