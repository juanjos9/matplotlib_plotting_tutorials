# Matplotlib Plotting Tutorials
# Polar Bar Plot

import numpy as np 
import matplotlib.pyplot as plt 

n = 21

# Data
theta = np.linspace(0, 2.0*np.pi, n)
heights = np.random.randn(n)

# Get an axes handle object
ax1 = plt.subplot(111, polar = True)

# Plot 
bars = ax1.bar(theta, heights,
            #    color = 'xkcd:salmon',
               color = plt.cm.jet(heights),
               width = 0.5,
               bottom = 0.0,
               edgecolor = 'k',
               alpha = 0.5,
               label = 'bars')

# Main tweaks
# Radius limits
ax1.set_ylim(0, 1.5)
# Radius Ticks
ax1.set_yticks(np.linspace(0,1.5,4))
# Radius ticks position in degrees
ax1.set_rlabel_position(135)
# Angle tick
ax1.set_xticks(np.linspace(0,2.0*np.pi, 17)[:-1])

# Additional Tewaks
plt.grid(True)
plt.legend()
plt.title('Polas Bar Plots')

plt.show()