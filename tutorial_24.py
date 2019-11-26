import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
mpl.style.use('default')

n = 201
x  = np.linspace(0, 4*np.pi, n)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2 

# Opening a figure
# Not needed for this example, but it is preferred for organization
plt.figure()

# Plot 1 - sin curve
plt.subplot(3,1,1)
plt.plot(x, y1, color = 'xkcd:azure', linestyle = '--', label = 'sine')
plt.title('Simple sine, cosine plot')
plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()

# Plot 2 - cosine curve
plt.subplot(3,1,2)
plt.plot(x, y2, color = 'xkcd:salmon', linestyle = '-', label = 'cosine')
# plt.title('Simple sine, cosine plot')
plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.grid()
plt.legend() 

# Plot 3 - cosine curve
plt.subplot(3,1,3)
plt.plot(x, y3, color = 'xkcd:green', marker = 'o', label = 'sine + cosine')
# plt.title('Simple sine, cosine plot')
plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()

# To make plots spread out evenly
plt.tight_layout()

# Use it once per figure
plt.show()
