import matplotlib.pyplot as plot

align_list = ('center', 'bottom', 'top', 'baseline')

ax1 = plot.axes()
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

for i, align in enumerate(align_list):
	plot.text(3 * i, 0, 'align=\'%s\'' % align, ha = 'center', va = align)

plot.plot([-3, 3 * len(align_list)], [0, 0], c = '#808080', ls = '--')
plot.scatter([3 * i for i in range(len(align_list))], [0] * len(align_list))

plot.show()
