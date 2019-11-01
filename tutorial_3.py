# Plotting tutorial in python 

# SUPERIMPOSITION TUTORIAL (PLOT TWO CURVES IN THE SAME GRAPH)

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,2.0*np.pi, 101)
y = np.sin(x)
z = np.cos(x)

x_numbers = np.linspace(0,7,15)
y_numbers = np.linspace(-1,1,11)

# FIRST WAY, I DON'T LIKE IT
# plt.plot(x,y,'r', x, z, 'g')
# plt.xlabel('Angle in radians')
# plt.ylabel('Magnitude')
# plt.title('Plot of some trigonometric functions')
# plt.xticks(x_numbers)
# plt.yticks(y_numbers)
# plt.axis([0, 6, -1.1, 1.1])
# plt.legend(['sine', 'cosine'])

# SECOND WAY, IT'S BETTER FOR ME 
plt.plot(x,y, color = 'r', label = 'sine')
plt.plot(x,z, color = 'g', label = 'cosine')
plt.xlabel('Angle in radians')
plt.ylabel('Magnitude')
plt.title('Plot of some trigonometric functions')
plt.xticks(x_numbers)
plt.yticks(y_numbers)
plt.axis([0, 6, -1.1, 1.1])
plt.legend()

plt.grid()
plt.show()