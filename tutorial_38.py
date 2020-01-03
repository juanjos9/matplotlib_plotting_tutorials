# Matplotlib Plotting Tutorials
# Colour Maps in Matplotlib
# Reference: https://matplotlib.org/example/color/colormaps_reference.html

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

breaks1 = np.linspace(-1.0, 1.0, 10)
breaks2 = np.linspace(0.0, 2.0, 10)

mpl.rcParams['contour.negative_linestyle'] = 'solid'

plt.figure(figsize= (12,8))
plt.subplot(221)
CS1 = plt.contour(x1, x2, Z,
                  breaks1,
                #   cmap = 'seismic',
                  colors = 'k',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

CS2 = plt.contourf(x1, x2, Z,
                  breaks1,
                #   cmap = 'seismic',
                  colors = 'k',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

plt.colorbar(ticks = breaks1, orientation = 'vertical')
plt.clabel(CS1, inline = 1, fontsize = 10,
        #    manual = manual_locations, # Pass a list of tuples for coordinates of labels
           )

plt.xlabel('angles 1')
plt.ylabel('angles 2')
plt.grid()
plt.title('Sine Cosine Wave - Diverging')

plt.subplot(222)
CS1 = plt.contour(x1, x2, Z+1,
                  breaks2,
                #   cmap = 'seismic',
                  colors = 'k',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

CS2 = plt.contourf(x1, x2, Z+1,
                  breaks2,
                #   cmap = 'seismic',
                  cmap = 'Greys',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

plt.colorbar(ticks = breaks2, orientation = 'vertical')
plt.clabel(CS1, inline = 1, fontsize = 10,
        #    manual = manual_locations, # Pass a list of tuples for coordinates of labels
           )

plt.xlabel('angles 1')
plt.ylabel('angles 2')
plt.grid()
plt.title('Sine Cosine Wave - Sequential') 

plt.subplot(223)
CS1 = plt.contour(x1, x2, Z,
                  breaks1,
                #   cmap = 'seismic',
                  colors = 'k',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

CS2 = plt.contourf(x1, x2, Z,
                  breaks1,
                #   cmap = 'seismic',
                  cmap = 'Accent',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

plt.colorbar(ticks = breaks1, orientation = 'vertical')
plt.clabel(CS1, inline = 1, fontsize = 10,
        #    manual = manual_locations, # Pass a list of tuples for coordinates of labels
           )

plt.xlabel('angles 1')
plt.ylabel('angles 2')
plt.grid()
plt.title('Sine Cosine Wave - Qualitative')

plt.subplot(224)
CS1 = plt.contour(x1, x2, Z+1,
                  breaks1,
                #   cmap = 'seismic',
                  colors = 'k',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

CS2 = plt.contourf(x1, x2, Z+1,
                  breaks1,
                #   cmap = 'seismic',
                  cmap = 'Accent',
                #   colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'xkcd:chocolate',
                #             'xkcd:beige', 'xkcd:salmon', 'xkcd:azure'),
                  extend = 'both', vmin = -1.0, vmax = 1.0
                  )

plt.colorbar(ticks = breaks1, orientation = 'vertical')
plt.clabel(CS1, inline = 1, fontsize = 10,
        #    manual = manual_locations, # Pass a list of tuples for coordinates of labels
           )

plt.xlabel('angles 1')
plt.ylabel('angles 2')
plt.grid()
plt.title('Sine Cosine Wave - Qualitative')

plt.show()
