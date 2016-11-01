import matplotlib.pyplot as plot

data = [[5., 25., 50., 20.],
        [4., 23., 51., 17.],
        [6., 22., 52., 19.]]

color_list = ['b', 'g', 'r']

gap = .8 / len(data)
for i, row in enumerate(data):
	plot.bar([x + i * gap for x in range(len(row))], row, width = gap, color = color_list[i])

plot.show()
