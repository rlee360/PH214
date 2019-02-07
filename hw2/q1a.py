import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib import rc
rc('text', usetex=True)

#defining arrow plotter - requires that ax be defined, e.g: ax = plt.subplot(111, projection='polar')
def vectArrow(x0, y0, xEnd, yEnd, faceColor, edgeColor):
    ax.annotate("", xytext=(x0,y0), xy=(xEnd,yEnd), arrowprops=dict(facecolor=faceColor, ec=edgeColor,alpha=0.5))
    
def vectEx(xPoint, yPoint, size, color):
    factor = 15
    plt.plot(xPoint, yPoint, marker=r'$\bigotimes$', markersize=size, markeredgewidth=0.3, markeredgecolor=color, markerfacecolor='k')
    #plt.plot(xPoint, yPoint, 'o', markersize=size, markeredgewidth=5, markeredgecolor=color, markerfacecolor='None')
    #plt.plot(xPoint, yPoint, 'x', markersize=size-factor, markeredgewidth=5, markeredgecolor=color, markerfacecolor='None')

#defining the circle
theta = np.linspace(0, 2*np.pi, num=1000)
r = 0.5*np.ones(1000)

#Some axes definitions
ax = plt.subplot(111, projection='polar')
#ax.plot(theta, r)
ax.plot(theta, 3.2*2*r, 'w-',alpha=0)

ax.set_rmin(0)
ax.set_rmax(5)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_yticklabels([])

ax.tick_params(axis='both', which='major', labelsize=50)
#ax.tick_params(axis='both', which='minor', labelsize=50)

Rtheta = (np.pi * np.array([1/6, 1/4, 1/3, 1/2])).tolist()
Rr = (2*np.ones(len(Rtheta))).tolist() #(np.sin(x)).tolist() #plot them based on function here


Stheta = np.pi * np.array([1/6, 1/4, 1/3, 1/2])
Sr = (np.sin(Stheta)).tolist()
Stheta.tolist()

Etheta = (np.pi * np.array([1/6, 1/4, 1/3, 1/2]))
print(Etheta)
Er = 0.5*np.sin(Etheta)#).tolist()
Etheta = (Etheta+np.pi/2).tolist()

for i in range(0, len(Rtheta)):
    vectArrow(0, 0, Rtheta[i], Rr[i], 'red','black') # plot R vector
    vectArrow(Rtheta[i], Rr[i], Stheta[i], Rr[i] + Sr[i], 'yellow','black') # plot S vector
    
    p = Etheta[i]
    q = Er[i]
    s = Rtheta[i]
    t = Rr[i]
    x = q * np.cos(p) + t*np.cos(s)
    y = q * np.sin(p) + t*np.sin(s)
    rnew = np.sqrt( x*x + y*y )
    thetanew = np.arctan2(y,x)
    print(str(rnew) + ", " + str(thetanew))
    vectArrow(s, t, thetanew, rnew, 'blue','black') # plot E vector
    vectEx(Rtheta[i], Rr[i], 30, 'white') # plot B vector


#legend stuff
legend_elements = [Patch(facecolor='red', edgecolor='black',
                         label='R vector',alpha=0.5),
                   Patch(facecolor='blue', edgecolor='black',
                         label='E vector',alpha=0.5),
                   Patch(facecolor='yellow', edgecolor='black',
                         label='S vector',alpha=0.5),
                   Line2D([0], [0], marker=r'$\bigotimes$', color='w', label='B Vector',
                          markerfacecolor='k', markersize=30, markeredgewidth=0.3, markeredgecolor='white')]
                          
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(-0.4, 1.05), ncol=1, fancybox=True, shadow=True, prop={'size': 50})

plt.title(r"\textbf{E}, \textbf{S} and \textbf{B} as a function of $\theta$", fontsize=60)

plt.show()
