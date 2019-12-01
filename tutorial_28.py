import numpy as np 
import matplotlib.pyplot as plt 

def vander_pol_oscillator(m,x,y):
    u, v = m*(x-x**3/3 - y), x/m
    return u, v

# Half length of dimension in x and y axis
l = 8.0

# No. of points along x/y axis
n = 101

# Parameter
mu = 0.5

# X and Y dimensions
x1 = np.linspace(-l,l,n)
x2 = np.linspace(-l,l,n)

# Creating a meshfield 
X1, X2 = np.meshgrid(x1, x2)

# Calculating velocities
U, V = vander_pol_oscillator(mu, X1, X2)

# Resultant velocity
vels = (U**2 + V**2)**0.5

# Line width parameter
lw = 4*vels/np.max(vels)

# Axes.streamplot(x,y, u,v, density = 1, linewidth = None, color = None, 
# cmap = None, norm = None, arrowsize = 1, arrowstyle = '-|>', minlength = 0.1,
# transform = None, zorder = None, start_points = None)  

plt.figure()
stream = plt.streamplot(X1, X2, # x and y coordinate positions
               U, V, # U and V velocities
               arrowsize = 2, # arrow size
               arrowstyle = '->', # arrow style
            #    color = 'xkcd:azure', # single color, cmap not needed
               color = vels, 
            #    density = 2, # density of streamlines
            #    density = (0.5, 3), # density along x and y directions - 2 value array
               # linewidth = 2, # linewidth
               linewidth = lw,
               cmap = plt.cm.jet # color map
               )

plt.title('Van der pol phase portrait')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(stream.lines)
plt.xticks()
plt.yticks()
plt.axis([-l, l, -l, l])
plt.grid()

plt.show()