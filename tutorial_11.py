import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

mean = 100
sd = 15
N = 1000
binsize = 20  
IQ = np.random.normal(mean, sd, N)

# plt.hist(IQ, binsize, facecolor = 'chocolate', label = 'IQs', normed = False)
counts, bins, extras = plt.hist(IQ, binsize, facecolor = 'chocolate', label = 'IQs', normed = False)
plt.plot(bins[1:], counts, label = 'series', color = 'xkcd:navy blue') #needs to extract bins counts (line13)
plt.xlabel('IQ')
plt.ylabel('Count/Fraction')
plt.xticks(bins) # needs to extract bins (line13)
plt.title('IQ distribution histogram')
plt.grid(True)
plt.legend()
plt.show()