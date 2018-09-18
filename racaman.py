import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

width = 230.
racaman_sequence_length = 102

def racaman_generator(n):
    current = 0
    s = set()
    for i in range(1, n):
        s.add(current)
        if current > 0:
            yield current
        if current - i > 0 and current - i not in s:
            current -= i
        else:
            current += i

fig = plt.figure(facecolor='w',figsize=(11.,11.))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.grid(True)
ax.set_xlim([0, width])
ax.set_ylim([0, width])
ax.axis('off')

last = 0.
flip = True
t1, t2 = 0, 180
for i, r in enumerate(racaman_generator(racaman_sequence_length)):
    x_coord = (last + r) / 2.
    last = r
    t1, t2 = t2, t1 # flip semi circle
    arc = mpatches.Arc([x_coord, width/2], i + 1, i + 1, angle=0, theta1=t1, theta2=t2)
    ax.add_patch(arc)

plt.show()
