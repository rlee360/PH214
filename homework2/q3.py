import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

Emag = 1
omega = 1
T = 2*np.pi/omega

ang = np.linspace(0, T , 10000)
eps = np.pi*1.5


x = Emag*np.cos(ang + eps)
y = 2*Emag*np.cos(ang)

fig, ax = plt.subplots()
ax.text(0.5, 0.5, 'Origin',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='green', fontsize=20)
        
ax.text(0.8, 0.05, 'The units of the x and y-axes can be \nrescaled depending on $E_0$ and $\omega$',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='green', fontsize=20)

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

plt.show()
