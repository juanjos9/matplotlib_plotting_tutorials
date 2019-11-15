import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.0*np.pi, 2.0*np.pi, 201)
y = np.sin(x)

plt.axhline(y = 0, color = 'k')
plt.axvline(x = 0, color = 'k')

# full hand standad color notation
# plt.plot(x,y, color = 'c', label = 'sin')

# RGB values: 0 -> no color, 1 -> full color
plt.plot(x,y, color =(0, 1, 0), label = 'sin')

# RGB normalization - divide each entry by 255
# plt.plot(x,y, color = (183/255, 20/255, 169/255), label = 'sin')

# RGBA values: 1 -> opaque, 0 -> full transparent  
# plt.plot(x,y, color =(0, 0, 1, 0.5), label = 'sin')

# RGB normalization - and transparency (divided by 100)
# plt.plot(x,y, color = (183/255, 20/255, 169/255, 10,100), label = 'sin')

# RGB/RGBA hex string value - it can be lowercase or uppercase
# plt.plot(x, y, color = '#B714A9', label = 'sin')

# Gray scale: 0 -> black, 1 -> white
# plt.plot(x,y, color = '0.5', label = 'sin')

plt.show()