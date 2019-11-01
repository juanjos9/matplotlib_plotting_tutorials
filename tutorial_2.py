# Plotting tutorial in python 

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,2.0*np.pi, 101)
y = np.sin(x)

x_numbers = np.linspace(0,7,15)
y_numbers = np.linspace(-1,1,11)

plt.plot(x,y, color = 'r', label = 'sin')
plt.xlabel('Angle in radians')
plt.ylabel('Magnitude')
plt.title('Plot of some trigonometric functions')
plt.xticks(x_numbers)
plt.yticks(y_numbers)
plt.axis([0, 6, -1.1, 1.1])
plt.legend()
plt.grid()
plt.show()