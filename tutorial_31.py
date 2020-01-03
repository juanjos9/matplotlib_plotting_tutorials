# Matplotlib Plotting Tutorials
# Polar Scatter plots

import numpy as np 
import matplotlib.pyplot as plt 

n = 101

# Data
theta = np.linspace(0, 2.0*np.pi, n)
curve1 = np.linspace(0, 1.0, n)
curve2 = curve1 + 0.1*np.random.uniform(-1,1,n)
curve3 = np.random.random(n)

# Get an axes handle object
ax1 = plt.subplot(111, polar = True)

# Scatter Plot
# ax1.plot(theta, curve1, label = 'mean', color = 'xkcd:salmon')
# ax1.scatter(theta, curve2, c = 'k', label = 'deviation')
ax1.scatter(theta, curve3,
            c = curve3,
            s = 400.0*np.abs(curve3),
            label = 'scatter',
            cmap = plt.cm.hsv,
            # c = 'yellow',
            alpha = 0.75,
            edgecolor = 'k')

# Main Tweks
# Radius limits   
ax1.set_ylim(0,1.5)         
# Radius ticks
ax1.set_yticks(np.linspace(0, 1.5, 4))
# Radius ticks position in degrees
ax1.set_rlabel_position(135)
#Angle ticks
ax1.set_xticks(np.linspace(0, 2.0*np.pi, 17)[:-1])

# Additional tweaks
plt.grid(True)
plt.legend()
plt.title('Polar Scatter Plots')

plt.show()