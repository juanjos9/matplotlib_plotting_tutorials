# Matplotlib Plotting Tutorials
# Contour/contourf Plot

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl

mpl.style.use('default')

n1 = 101
n2 = 51

x1 = np.linspace(0, 2.0*np.pi, n1)
x2 = np.linspace(0, 2.0*np.pi, n2)

X1, X2 = np.meshgrid(x1, x2)

Z = np.sin(X1)*np.cos(X2)

breaks = np.linspace(-1, 1, 11)

mpl.rcParams['contour.negative_linestyle'] = 'solid'

plt.figure()
# CS1 = plt.contour(x1, x2, Z,
#                   breaks,
#                   cmap = 'seismic',
#                 #   color = 'k',
#                   color = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
#                            'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
#                   extend = 'both', vmin = -1.0, vmax = 1.0
#                   )

CS2 = plt.contourf(x1, x2, Z,
                   breaks,
                   cmap = 'seismic',
                #    colors = 'k',
                #    colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #              'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                   extend = 'both', vmin = -1.0, vmax = 1.0
                   )

# plt.clabel(CS2, inline = 1, fontsize = 10)
plt.colorbar(ticks = breaks, orientation = 'vertical')

plt.xlabel('angles 1')
plt.ylabel('angles 2')
plt.grid()
plt.title('Sine Cosine Wave')

plt.show()
