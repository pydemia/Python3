import wx, numpy

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure



def supershape_radius(phi, a, b, m, n1, n2, n3):
	theta = .25 * m * phi
	cos = numpy.fabs(numpy.cos(theta) / a) ** n2
	sin = numpy.fabs(numpy.sin(theta) / b) ** n3
	r = (cos + sin) ** (-1. / n1)
	r /= numpy.max(r)
	return r



class SuperShapeFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title,
		                  style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,
		                  size = (480, 480))
		self.fig = Figure((6, 6), dpi = 80)

		self.panel = wx.Panel(self, -1)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(FigureCanvasWxAgg(self.panel, -1, self.fig), 1)
		self.panel.SetSizer(sizer)

		self.draw_figure()

	def draw_figure(self):
		phi = numpy.linspace(0, 2 * numpy.pi, 1024)
		r = supershape_radius(phi, 1, 1, 3, 2, 18, 18)
		ax = self.fig.add_subplot(111, polar = True)
		ax.plot(phi, r, lw = 3.)

		self.fig.canvas.draw()



app = wx.App(redirect = True)
top = SuperShapeFrame(None, -1, 'SuperShape')
top.Show()
app.MainLoop()
