import random
import matplotlib.cm as cm
import matplotlib.colors as col
import matplotlib.pyplot as plot

values = [random.randint(0, 99) for i in range(50)]
values.sort()

cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)

plot.bar(range(len(values)), values, color = cmap.to_rgba(values))
plot.show()
