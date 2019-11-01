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
curve1 = ax1.plot(x,y, label = 'sin', color = 'r')
curve2 = ax2.plot(x,z, label = 'sinh', color = 'g')

# plt.xlabel('Angle in radians')
# plt.ylabel('Magnitude')
plt.title('Plot of some trigonometric functions')
# plt.xticks(x_numbers)
# plt.yticks(y_numbers)
# plt.axis([0, 6, -1.1, 1.1])
plt.legend()

# plt.grid()
plt.show()