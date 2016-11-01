import numpy
import matplotlib.pyplot as plot

data = numpy.random.randn(100, 5)

plot.boxplot(data)
plot.show()
