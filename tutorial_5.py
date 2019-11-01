# Plotting tutorial in python 

# MULTIPLE PLOTS WITH THE SAME X AXIS (DIFFERENT Y AXIS)

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,2.0*np.pi, 101)
y = np.sin(x)
z = np.sinh(x)

# Values for making ticks in x and y axis
x_numbers = np.linspace(0,7,15)
y_numbers1 = np.linspace(-1,1,11)
y_numbers2 = np.linspace(0,300,7)

# Separate the figure object and axes object from the plotting object
fig, ax1 = plt.subplots()

# Duplicate the axes with a different y axis an the same x axis
ax2 = ax1.twinx()

# Plot the curves on ax1 and ax2, and get the curves handles
curve1, = ax1.plot(x,y, label = 'sin', color = 'r')
curve2, = ax2.plot(x,z, label = 'sinh', color = 'g')

# Make a curves list to access the parameters in the curves
curves = [curve1, curve2]

# Add legend via axes 1 or axes 2 object
ax1.legend(curves, [curve.get_label() for curve in curves])
# ax2.legend(curves, [curve.get_label() for curve in curves]) # Also valid

# X axis label via the axes
ax1.set_xlabel('Angle/Value', color = curve1.get_color())
# ax1.set_xlabel('Angle/Value', color = curve1.get_color()) # it doesn't work, 
# ax2 has no property control over x axis (label, grid, color)

# Y axis label via the axes
ax1.set_ylabel('Magintude', color = curve1.get_color())
ax2.set_ylabel('Magnitude', color = curve2.get_color())

# Y ticks - make them colored as well
ax1.tick_params(axis = 'y', colors = curve1.get_color())
ax2.tick_params(axis = 'y', colors = curve2.get_color())

# Set X ticks, one command is usually sufficient and both of them work
ax1.set_xticks(x_numbers)

# Set Y ticks
ax1.set_yticks(y_numbers1)
ax2.set_yticks(y_numbers2)

# Grids
ax1.grid(color = curve2.get_color())
ax2.grid(color = curve2.get_color())
ax1.yaxis.grid(False)


plt.title('Plot of some trigonometric functions')
plt.legend()

# plt.grid()
plt.show()