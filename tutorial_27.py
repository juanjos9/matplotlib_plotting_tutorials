import numpy as np 
import matplotlib.pyplot as plt   
import matplotlib.gridspec as gs

# Simple figure - no spans
# Create the figure 
fig1 = plt.figure(1)

# Create a gridspec object
gs1 = gs.GridSpec(nrows = 2, ncols = 2)

# Axis handle for plot 1
ax1 = plt.subplot(gs1[0,0])
ax1.text(x = 0.5, y = 0.5, s = 'ax1', va = 'center', ha = 'center')

# Axis handle for plot 2
ax2 = plt.subplot(gs1[0,1])
ax2.text(x = 0.5, y = 0.5, s = 'ax2', va = 'center', ha = 'center')

# Axis handle for plot 3
ax3 = plt.subplot(gs1[1,0])
ax3.text(x = 0.5, y = 0.5, s = 'ax3', va = 'center', ha = 'center')

# Axis handle for plot 4
ax4 = plt.subplot(gs1[1,1])
ax4.text(x = 0.5, y = 0.5, s = 'ax4', va = 'center', ha = 'center')

plt.suptitle('Subplot via GridSpec')
plt.tight_layout()
plt.subplots_adjust(top = 0.9)

plt.show()

# Figure with row/column spans
# Create the figure
fig2 = plt.figure(2)

# Create the gridspec object
gs2 = gs.GridSpec(nrows = 3, ncols = 3)

# Axis handle for plot 1
ax1 = plt.subplot(gs2[0,0:3]) # Figure spans 3 columns
# ax1 = plt.subplot(gs2[0,:]) # Same as above
ax1.text(x=0.5, y =0.5, s='ax1', va='center', ha='center')

# Axis handle for plot 2
ax2 = plt.subplot(gs2[1,0:2])
ax2.text(x=0.5, y =0.5, s='ax2', va='center', ha='center')

# Axis handle for plot 3
ax3 = plt.subplot(gs2[1:3,2])
ax3.text(x=0.5, y =0.5, s='ax3', va='center', ha='center')

# Axis handle for plot 4
ax4 = plt.subplot(gs2[2,0])
ax4.text(x=0.5, y =0.5, s='ax4', va='center', ha='center')

# Axis handle for plot 5
ax5 = plt.subplot(gs2[2,1])
ax5.text(x=0.5, y =0.5, s='ax5', va='center', ha='center')

plt.suptitle('Subplot via GridSpec')
plt.tight_layout()
plt.subplots_adjust(top = 0.9)

# I can create a gridspec inside other gridspec. I found this innecesary and I didn't 
# add it to this piece of code. For more information about this topic, we can refer to the 
# matplotlib page

plt.show()