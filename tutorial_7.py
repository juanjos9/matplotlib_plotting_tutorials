# Plotting tutorial in python 

# Moving the X and Y axis

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2.0*np.pi, 2.0*np.pi, 201)
y = np.sin(x)
z = np.cos(x)

# x_numbers = np.linspace(0,7,15)
# y_numbers = np.linspace(-1,1,11)

plt.plot(x,y, color = 'r', label = 'sine')
plt.plot(x,z, color = 'g', label = 'cosine')

plt.title('Plot of some trigonometric functions')
plt.legend()

# Push the X axis up
plt.axes().spines['bottom'].set_position(('data', 0))

# Push the Y axis right
plt.axes().spines['left'].set_position(('data', 0))

# Add a horizontal line at the bottom
plt.axhline(y=plt.ylim()[0], color = 'k')

# Add a vertical line at the left
plt.axvline(x=plt.xlim()[0], color = 'k')

plt.xlabel('Angle in radians')
plt.ylabel('Magnitude')


plt.grid()
plt.show()