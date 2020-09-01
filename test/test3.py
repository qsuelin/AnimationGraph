import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create some artists at the initialisation stage
# Update their coordinates in the update function
# Don't forget to return a list of updated artists.
#
# fargs: tuple or None, optional
#
# Additional arguments to pass to each call to func.


# x = np.arange(130, 190, 1)
# y = 97.928 * np.exp(- np.exp(-  0.1416 *( x - 146.1 )))
# z = 96.9684 * np.exp(- np.exp(-0.1530*( x - 144.4)))
#
# fig, ax = plt.subplots()
# line1, = ax.plot(x, y, color = "r")
# line2, = ax.plot(x, z, color = "g")
#
# def update(num, x, y, z, line1, line2):
#     line1.set_data(x[:num], y[:num])
#     line2.set_data(x[:num], z[:num])
#     return [line1,line2]
#
# ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, z, line1, line2],
#                   interval=295, blit=True)
#
# ax.set_xlabel('Age (day)')
# ax.set_ylabel('EO (%)')
#
# plt.show()

import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random

fig = plt.figure()
ax1 = plt.axes(xlim=(-108, -104), ylim=(31,34))
line, = ax1.plot([], [], lw=2)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plotlays, plotcols = [2], ["black","red"]
lines = []
for index in range(2):
    lobj = ax1.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines

x1,y1 = [],[]
x2,y2 = [],[]

# fake data
frame_num = 100
gps_data = [-104 - (4 * random.rand(2, frame_num)), 31 + (3 * random.rand(2, frame_num))]


def animate(i):

    x = gps_data[0][0, i]
    y = gps_data[1][0, i]
    x1.append(x)
    y1.append(y)

    x = gps_data[0][1,i]
    y = gps_data[1][1,i]
    x2.append(x)
    y2.append(y)

    xlist = [x1, x2]
    ylist = [y1, y2]

    #for index in range(0,1):
    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum]) # set data for each line separately.

    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=20, blit=True)


plt.show()