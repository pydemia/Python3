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



class LinearScaling(object):
	def __init__(self, src_range, dst_range):
		self.src_start, src_diff = src_range[0], src_range[1] - src_range[0]
		self.dst_start, dst_diff = dst_range[0], dst_range[1] - dst_range[0]
		self.src_to_dst_coeff = dst_diff / src_diff
		self.dst_to_src_coeff = src_diff / dst_diff

	def src_to_dst(self, X):
		return (X - self.src_start) * self.src_to_dst_coeff + self.dst_start

	def dst_to_src(self, X):
		return (X - self.dst_start) * self.dst_to_src_coeff + self.src_start



class SuperShapeFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title,
		                  style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,
		                  size = (480, 640))
		self.m = 3

		self.n1 = 2
		self.n1_scaling = LinearScaling((.01, 20), (0, 200))

		self.n2 = 18
		self.n2_scaling = LinearScaling((.01, 20), (0, 200))

		self.n3 = 18
		self.n3_scaling = LinearScaling((.01, 20), (0, 200))

		self.fig = Figure((6, 6), dpi = 80)

		panel = wx.Panel(self, -1)

		self.m_slider = wx.Slider(panel, -1, self.m, 1, 20, size = (250, -1), style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
		self.n1_slider = wx.Slider(panel, -1, self.n1_scaling.src_to_dst(self.n1), 0, 200, size = (250, -1), style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
		self.n2_slider = wx.Slider(panel, -1, self.n1_scaling.src_to_dst(self.n2), 0, 200, size = (250, -1), style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
		self.n3_slider = wx.Slider(panel, -1, self.n1_scaling.src_to_dst(self.n3), 0, 200, size = (250, -1), style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

		self.m_slider.Bind(wx.EVT_SCROLL, self.on_m_slide)
		self.n1_slider.Bind(wx.EVT_SCROLL, self.on_n1_slide)
		self.n2_slider.Bind(wx.EVT_SCROLL, self.on_n2_slide)
		self.n3_slider.Bind(wx.EVT_SCROLL, self.on_n3_slide)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(FigureCanvasWxAgg(panel, -1, self.fig), 0, wx.TOP)
		sizer.Add(self.m_slider,  0, wx.ALIGN_CENTER)
		sizer.Add(self.n1_slider, 0, wx.ALIGN_CENTER)
		sizer.Add(self.n2_slider, 0, wx.ALIGN_CENTER)
		sizer.Add(self.n3_slider, 0, wx.ALIGN_CENTER)
		panel.SetSizer(sizer)

		self.draw_figure()

	def on_m_slide(self, event):
		self.m = self.m_slider.GetValue()
		self.refresh_figure()

	def on_n1_slide(self, event):
		self.n1 = self.n1_scaling.dst_to_src(self.n1_slider.GetValue())
		self.refresh_figure()

	def on_n2_slide(self, event):
		self.n2 = self.n2_scaling.dst_to_src(self.n2_slider.GetValue())
		self.refresh_figure()

	def on_n3_slide(self, event):
		self.n3 = self.n3_scaling.dst_to_src(self.n3_slider.GetValue())
		self.refresh_figure()

	def refresh_figure(self):
		r = supershape_radius(self.phi, 1, 1, self.m, self.n1, self.n2, self.n3)
		self.l.set_ydata(r)
		self.fig.canvas.draw_idle()
	
	def draw_figure(self):
		self.phi = numpy.linspace(0, 2 * numpy.pi, 1024)
		r = supershape_radius(self.phi, 1, 1, self.m, self.n1, self.n2, self.n3)
		ax = self.fig.add_subplot(111, polar = True)
		self.l, = ax.plot(self.phi, r, lw = 3.)

		self.fig.canvas.draw()



app = wx.App(redirect = True)
top = SuperShapeFrame(None, -1, 'SuperShape')
top.Show()
app.MainLoop()
