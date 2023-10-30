import matplotlib.pyplot as plt
import numpy as np
from math import pi


for theta in np.arange(0, 2 * pi, 0.01, dtype=complex):
    for E in np.arange(0, 1.6, 0.2, dtype=complex):
        r = E * np.sin(theta)**(2)
        x = r * np.sin(theta)
        y = r * np.cos(theta)
        plt.plot(x, y, 'k,')
        
    for V in np.arange(0, 1.6, 0.2, dtype=complex):
        R = V * np.cos(theta)**(1/2)
        r = (R.real**2+R.imag**2)**(1/2)
        x = r * np.sin(theta)
        y = r * np.cos(theta)
        # plot solid line
        plt.plot(x, y, 'r,') 
for i in np.arange(0.2, 1.6, 0.2):
    plt.plot(i, 0, 'kv', markersize=3)
    plt.plot(-i, 0, 'kv', markersize=3)

ax = plt.gca()
ax.set_aspect("equal")
plt.xlabel('x')  
plt.ylabel('y',rotation='horizontal') 
plt.figtext(0.3,0.93,"BLACK: Electric Field Lines", color='k', ha='left')
plt.figtext(0.3,0.9,"RED:     Equipotential Lines", color='r', ha='left') 
plt.show()
