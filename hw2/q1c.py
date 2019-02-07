import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('text', usetex=True)

#define x's
theta = np.linspace(0, 2*np.pi, num=10000) #[0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 1] #
theta = np.pi*np.array(theta)

#find the lengths of the vectors
r = np.sin(theta) * np.sin(theta)

#for use with arrow plotting
thetahat = theta.tolist()
rhat = r.tolist()

#define plot
ax = plt.subplot(111, projection='polar')

# plot the vectors that we want we want
#for i in range(0, len(theta)):
#    ax.annotate("", xytext=(0.0,0.0), xy=(thetahat[i],rhat[i]), arrowprops=dict(facecolor='black'))

ax.plot(theta,r)
ax.set_rmin(0)
ax.set_rmax(1.2)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_yticklabels([]) 

ax.tick_params(axis='both', which='major', labelsize=50)
plt.title(r"Path of \textbf{S} as a Function of $\theta$, Continuously", fontsize=60)

plt.show()
