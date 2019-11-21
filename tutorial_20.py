import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')

x = np.linspace(0, 2*np.pi, 101)
c, s = np.cos(x), np.sin(x)

plt.plot(x,c, color = 'r', label = 'cosine')
plt.plot(x,s, color = 'g', label = 'sine')

plt.plot(0.5*np.pi, np.sin(0.5*np.pi), 'bo')
plt.plot(1.5*np.pi, np.sin(1.5*np.pi), 'ko')  

plt.annotate(s = 'sine local maxima', xy = (0.5*np.pi, np.sin(0.5*np.pi)), 
xytext = (1.0*np.pi, np.sin(0.5*np.pi)), arrowprops= dict(facecolor = 'blue', shrink = 1))

plt.grid()
plt.legend()
plt.title('Sample sine and cosine curves') 

plt.show()