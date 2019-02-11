import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = '-'
mpl.rcParams['grid.linewidth'] = 0.5

from matplotlib import rc
rc('text', usetex=True)

#define x's
theta = [0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 1] #np.linspace(0, 2*np.pi, num=10000) #
theta = np.pi*np.array(theta)

#find the lengths of the vectors
r = np.sin(theta) * np.sin(theta)

#for use with arrow plotting
thetahat = theta.tolist()
rhat = r.tolist()

#define plot
ax = plt.subplot(111, projection='polar')

ax.plot(theta,r, linewidth=2)
ax.set_rmin(0)
ax.set_rmax(1.2)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_yticklabels([]) 

 # The next section is for the discrete vectors. Remember to change the theta above, and the title below. Comment up to the tick_params.
#plot the vectors that we want we want
for i in range(0, len(theta)):
    ax.annotate("", xytext=(0.0,0.0), xy=(thetahat[i],rhat[i]), arrowprops=dict(facecolor='black'))

strings = ['$0$', '$\pi/6$', '$\pi/4$', '$\pi/3$', '$\pi/2$', '$2\pi/3$','$3\pi/4$', '$5\pi/6$', '$\pi$']
textmvfactor = 0.015

for j in range(0, len(thetahat)):
    if j < len(thetahat)/2:
        ax.text(thetahat[j], rhat[j] + textmvfactor , strings[j], verticalalignment='bottom', horizontalalignment='center', color='green', fontsize=40)
    else:
        ax.text(thetahat[j], rhat[j] + textmvfactor , strings[j], verticalalignment='top', horizontalalignment='right', color='green', fontsize=40)


ax.tick_params(axis='both', which='major', labelsize=50)
plt.title(r"Path of \textbf{S} as a Function of $\theta$ in Discrete Steps", fontsize=60)

plt.show()
