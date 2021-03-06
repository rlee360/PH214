import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

Emag = 1
omega = 1
T = 2*np.pi/omega

ang = np.linspace(0, T , 10000)
eps = np.pi/6 # Change this for different phase differences.


x = Emag*np.cos(ang + eps)
y = 2*Emag*np.cos(ang)

fig, ax = plt.subplots()
ax.text(0.5, 0.5, 'Origin',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='green', fontsize=20)
        
ax.text(0.7, 0.05, 'The units of the x and\ny-axes can be rescaled\ndepending on $E_0$ and $\omega$',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='green', fontsize=20)

#X, Y = np.meshgrid(x,y)
#F = X**2 + Y**2 - 0.6
plt.plot(0,0,'ko')
plt.plot(x, y)
ax.set_xlim(-2, 2)
ax.set_ylim(-2.2, 2.2)

fs = 30
plt.title("Elliptically Polarized TEM Wave $\epsilon = 3\pi/2$", fontsize=fs+5)
plt.xticks( fontsize=fs-5)
plt.yticks(fontsize=fs-5)
plt.xlabel("x̂", fontsize=fs)
plt.ylabel("ŷ", fontsize=fs,rotation=0)

plt.gca().set_aspect('equal', adjustable='box') # makes the x and y axes 1-1 in lengths

plt.show()
