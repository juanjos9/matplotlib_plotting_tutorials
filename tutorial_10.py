import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl 
mpl.style.use('classic')
# print(mpl.style.available)

x = np.linspace(-2*np.pi, 2*np.pi, 201)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y, color = 'r', label = 'sin')
plt.plot(x,z, color = 'g', label = 'cos')

plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.title('Plot of sine and cosine')
plt.grid(True)
plt.legend()
plt.show()