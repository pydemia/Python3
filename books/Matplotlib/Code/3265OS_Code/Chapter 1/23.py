import random
import matplotlib.pyplot as plot
import matplotlib.tri as tri


count = 100
X = [random.random() for i in range(count)]
Y = [random.random() for i in range(count)]

triangles = tri.Triangulation(X, Y)

plot.triplot(triangles, 'bo-')
plot.show()
