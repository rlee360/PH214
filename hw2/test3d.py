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

fs=40
plt.title(r"3D Plot of \textbf{S} through $\theta$ and $\phi$", fontsize=fs+5)
plt.xticks( fontsize=fs-5)
plt.yticks(fontsize=fs-5)
#plt.xlabel("x̂", fontsize=fs)
#plt.ylabel("ŷ", fontsize=fs,rotation=0)

plt.show()
