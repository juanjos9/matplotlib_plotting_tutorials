# Matplotlib Plotting Tutorials
# Polar stream plot

import numpy as np 
import matplotlib.pyplot as plt 

# Domain details
Rmin = 0.0
Rmax = 4.0 
theta_min = 0.0
theta_max = 2.0*np.pi

# Number of point in total domain along x/y axis
n = 101

# Radius, theta
rad = np.linspace(Rmin, Rmax, n)
theta = np.linspace(theta_min, theta_max, n)

# Grid values
theta_matrix, radius_matrix = np.meshgrid(theta, rad)

# Flows/velocities
# U = radial, V = tangencial
# U, V = radius_matrix*(1.0-radius_matrix**2.0)*(4.0-radius_matrix**2.0), 2.0 - radius_matrix**2.0
U, V = np.ones((n,n)), np.ones((n,n))

# Resultant velocities
vels = (U**2.0 + (V*radius_matrix)**2.0)**0.5

# line width parameter
lw = 30*vels/np.max(vels)

# Get an axes hadle/object
ax1 = plt.subplot(111, polar = True)

stream = ax1.streamplot(theta_matrix, radius_matrix, V, U,
                        arrowsize = 2,
                        arrowstyle = '->',
                        color = 'xkcd:azure',
                        # color = vels,
                        density = 1,
                        # density = (0.5,1),
                        linewidth = 1,
                        # linewidth = lw,
                        cmap=plt.cm.jet
                        )

# Main tweaks
# Radius limits
ax1.set_ylim(0,4)                        
# Radius ticks
ax1.set_yticks(np.linspace(0,4,5))
# Radius tick position in degrees
ax1.set_rlabel_position(135)
# Angle ticks
ax1.set_xticks(np.linspace(0, 2.0*np.pi, 17)[:-1])

# Additional tweaks
plt.grid(True)
# plt.colorbar(stream.lines)
# plt.legend() - no label option, hence no legend
plt.title('Polar bar Plots')

plt.show()

