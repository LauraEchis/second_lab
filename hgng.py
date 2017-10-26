import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

# class HighlightSelected(lines.VertexSelector):
#     def __init__(self, line, fmt='ro', **kwargs):
#         lines.VertexSelector.__init__(self, line)
#         self.markers, = self.axes.plot([], [], fmt, **kwargs)
#
#     def process_selected(self, ind, xs, ys):
#         self.markers.set_data(xs, ys)
#         self.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
x=[-100, 100]
y=[-100*2+5, 100*2+5]
line, = ax.plot(x, y,  picker=5)

#selector = HighlightSelected(line)
plt.show()