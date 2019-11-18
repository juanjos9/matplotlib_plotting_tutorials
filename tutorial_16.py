import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

N = 1001
x = np.linspace(-2.0*np.pi, 2.0*np.pi, N)
y = np.random.normal(0,1,N) + np.sin(x)

# Default
plt.scatter(x,y)

plt.scatter(x, y, label = 'sin scatter', marker = '*', c = 'chocolate', s = 100, 
edgecolors= 'blue', alpha= 0.09, linewidths=1.5)

plt.xlabel('Angles')
plt.ylabel('Plots')
plt.title('Sample scatter plot:')
plt.grid()
plt.legend()
plt.show()