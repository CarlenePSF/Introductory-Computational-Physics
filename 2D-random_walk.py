"""
Simulation of a 2D random-walk with random number generator
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
from random import seed
from random import random

# seed random number generator
seed()

dict_constants = dict(N=25000, L=101, x0=0.0)


def random_integer(q0, n, length):
    q = list()
    for i in range(0, n, 1):
        q.append(q0)
        a = random()
        if a < 0.5:
            q0 = q0 + 1
            if q0 > length:
                q0 = q0 - 1
            elif q0 < 0:
                q0 = q0 + 1
        else:
            q0 = q0 - 1
            if q0 > length:
                q0 = q0 - 1
            elif q0 < 0:
                q0 = q0 + 1
    return q


x = random_integer(dict_constants['x0'], dict_constants['N'], dict_constants['L'])
y = random_integer(dict_constants['x0'], dict_constants['N'], dict_constants['L'])


mpl.rc('text', usetex=False)
mpl.rc('font', family='serif', weight='normal', style='normal', size='12')

font = {
    'family': 'serif',
    'color': 'darkned',
    'weight': 'normal',
    'size': 8,
    }
fig, (ax1) = plt.subplots(1, 1)
fig.suptitle('2D random walk')
ax1.plot(x, y, '-')
ax1.set_ylabel('$y$ position')
ax1.set_xlabel('$x$ position')

plt.show()
