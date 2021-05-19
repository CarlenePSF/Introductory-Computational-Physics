"""
Simulation of a 2D random-walk with random number generator
"""
import matplotlib.pyplot as plt
from random import seed
from random import random
from math import sqrt
import matplotlib as mpl

N = 25000
L = 101
x = []
y = []
v = []
x0 = 0.0
y0 = 0.0


# seed random number generator
seed()
# generate random integer values
for i in range(0, N, 1):
    x.append(x0)
    y.append(y0)
    a = random()
    if a < 0.5:
        x0 = x0+1
        if x0 > L:
            x0 = x0 - 1
        elif x0 < 0:
            x0 = x0 + 1
    else:
        x0 = x0-1
        if x0 > L:
            x0 = x0 - 1
        elif x0 < 0:
            x0 = x0 + 1
    b = random()
    if b < 0.5:
        y0 = y0+1
        if y0 > L:
            y0 = y0 - 1
        elif y0 < 0:
            y0 = y0 + 1
    else:
        y0 = y0-1
        if y0 > L:
            y0 = y0 - 1
        elif y0 < 0:
            y0 = y0 + 1
    v.append(sqrt(x0**2 + y0**2))

mpl.rc('text', usetex=True)
mpl.rc('font', family='serif', weight='normal', style='normal', size='12')

font = {'family': 'serif',
        'color': 'darkned',
        'weight': 'normal',
        'size': 8,
        }


#fig, (ax1, ax2) = plt.subplots(2, 1)
fig, (ax1) = plt.subplots(1, 1)
fig.suptitle('2D random walk')

ax1.plot(x, y, '-')
ax1.set_ylabel('$y$ position')
ax1.set_xlabel('$x$ position')
'''
ax2.plot(v, '.-')
ax2.set_ylabel('$d$ vector')
ax2.set_xlabel('step')
'''
plt.show()
