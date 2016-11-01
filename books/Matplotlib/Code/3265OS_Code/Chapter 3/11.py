import matplotlib.pyplot as plot

shape = plot.Circle((0, 0), radius = 1., color = '#8080f0')
plot.gca().add_patch(shape)

plot.grid(True)
plot.axis('scaled')
plot.show()
