import numpy
import matplotlib.pyplot as plot

arrow_style_list = ('<->', '<-', '->', 'wedge', 'fancy', 'simple')

ax1 = plot.axes()
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

plot.scatter([0] * len(arrow_style_list), range(len(arrow_style_list)), c = 'k')
plot.scatter([-.1, 2], [-1, len(arrow_style_list)], c = 'w', edgecolor = 'w')

for i, arrow_style in enumerate(arrow_style_list):
	plot.annotate('arrowstyle = "%s"' % arrow_style,
                ha = 'left', va = 'center',
                xytext = (.75, i+.5),
                xy = (.025, i),
                arrowprops = { 'arrowstyle' : arrow_style, 'facecolor' : 'k'})
plot.show()
