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



class SuperShapeWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title = 'SuperShape')
		
		layout_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
		self.add(layout_box)

		self.m = 3
		self.n1 = 2
		self.n2 = 18
		self.n3 = 18

		self.fig = Figure((6, 6), dpi = 80)

		#w, h = self.fig.get_size_inches()
		#dpi_res = self.fig.get_dpi()
		#w, h = int(numpy.ceil(w * dpi_res)), int(numpy.ceil(h * dpi_res))

		canvas = FigureCanvasGTK3Agg(self.fig)
		#canvas.set_size_request(w, h)
		layout_box.add(canvas)

		self.m_slider = Gtk.HScale.new(Gtk.Adjustment(self.m, 1, 20, 1., .1, 1))
		self.m_slider.connect('value-changed', self.on_m_slide)
		layout_box.add(self.m_slider)

		self.n1_slider = Gtk.HScale.new(Gtk.Adjustment(self.n1, .01, 20, 1., .1, 1))
		self.n1_slider.connect('value-changed', self.on_n1_slide)
		layout_box.add(self.n1_slider)

		self.n2_slider = Gtk.HScale.new(Gtk.Adjustment(self.n2, .01, 20, 1., .1, 1))
		self.n2_slider.connect('value-changed', self.on_n2_slide)
		layout_box.add(self.n2_slider)

		self.n3_slider = Gtk.HScale.new(Gtk.Adjustment(self.n3, .01, 20, 1., .1, 1))
		self.n3_slider.connect('value-changed', self.on_n3_slide)
		layout_box.add(self.n3_slider)

		self.draw_figure()

	def on_m_slide(self, event):
		self.m = self.m_slider.get_value()
		self.refresh_figure()

	def on_n1_slide(self, event):
		self.n1 = self.n1_slider.get_value()
		self.refresh_figure()

	def on_n2_slide(self, event):
		self.n2 = self.n2_slider.get_value()
		self.refresh_figure()

	def on_n3_slide(self, event):
		self.n3 = self.n3_slider.get_value()
		self.refresh_figure()

	def draw_figure(self):
		self.phi = numpy.linspace(0, 2 * numpy.pi, 1024)
		ax = self.fig.add_subplot(111, polar = True)
		r = supershape_radius(self.phi, 1, 1, self.m, self.n1, self.n2, self.n3)
		self.lines, = ax.plot(self.phi, r, lw = 3.)
		self.fig.canvas.draw()

	def refresh_figure(self):
		r = supershape_radius(self.phi, 1, 1, self.m, self.n1, self.n2, self.n3)
		self.lines.set_ydata(r)
		self.fig.canvas.draw_idle()



win = SuperShapeWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
