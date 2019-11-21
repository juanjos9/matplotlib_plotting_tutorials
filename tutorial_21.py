import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl 
mpl.style.use('default')

x = np.linspace(-2*np.pi, 2*np.pi, 201)
c, s = np.cos(x), np.sin(x)

plt.plot(x,c, color = 'b', label = 'cosine') 
plt.plot(x,s, color = 'r', label = 'sine')
# plt.fill_between(x,1,s)
# plt.fill_between(x, c, s, color = 'g', alpha = 0.4)
plt.fill_between(x,c,s, where=c>=s, color = 'green', alpha = 0.3)
plt.fill_between(x,c,s, where=c<=s, color = 'blue', alpha = 0.3) 


plt.grid()
plt.legend()
plt.title('Sample sine and cosine curves')
plt.show()