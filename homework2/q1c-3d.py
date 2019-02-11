import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

from matplotlib import rc
rc('text', usetex=True)

# https://plot.ly/~raccase/8/

Smag = 1; #modify this for the additional factors in the front

theta, phi = np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100)
THETA, PHI = np.meshgrid(theta, phi)
S = Smag * np.sin(PHI) * np.sin(PHI)
X = S * np.sin(PHI) * np.cos(THETA)
Y = S * np.sin(PHI) * np.sin(THETA)
Z = S * np.cos(PHI)
fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)

fs=35
plt.title(r"3D Plot of \textbf{S} through $\theta$ and $\phi$", fontsize=fs+5)
plt.xticks( fontsize=fs-5)
plt.yticks(fontsize=fs-5)
for t in ax.zaxis.get_major_ticks(): t.label.set_fontsize(fs-5)

ax.text(2, 0,0, "The three axes here are not representative of the spherical (r, $\\theta$, $\phi$) coordinates, but I could not figure out how to get polar axes in 3D.",
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='green', fontsize=fs)

#plt.xlabel("x̂", fontsize=fs)
#plt.ylabel("ŷ", fontsize=fs,rotation=0)

plt.show()
