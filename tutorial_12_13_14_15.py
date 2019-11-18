import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl 
mpl.style.use('classic')

range_vals = np.linspace(0,100, 11)

counts1 = np.random.rand(10)*4.0
counts2 = np.random.rand(10)*8.0
counts3 = np.random.rand(10)*2.0
errors = np.ones(10)*1.0
bar_width = 5

mid_vals = (range_vals[0:-1]+range_vals[1:])*0.5 -bar_width*0.5
# mid_vals = (range_vals[0:-1]+range_vals[1:])*0.5
groups = ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07', 'g08', 'g09', 'g10']   

# plt.bar(mid_vals, counts1)
# plt.bar(mid_vals, counts1, facecolor = 'chocolate', width = bar_width, label = 'sample bar1')
# plt.bar(mid_vals, counts1, facecolor = 'chocolate', width = bar_width, label = 'sample bar1', yerr = errors)
# plt.bar(mid_vals, counts2, facecolor = 'aquamarine', width = bar_width, label = 'sample bar2', yerr = errors)

# STACKS PLOTS (BARS OVER OTHER BARS AS BASE)
# plt.bar(mid_vals, counts2, bottom = counts1, color = 'aquamarine', width = bar_width, label = 'sample bar 2', yerr = errors) # For stacks plots
# plt.bar(mid_vals, counts3, bottom = counts1+counts2, color = 'beige', width = bar_width, label = 'sample bar 2', yerr = errors) # For stacks plots

# FOR HORIZONTAL BAR CHARTS
plt.barh(mid_vals, counts1, facecolor = 'chocolate', align = 'center', height = bar_width, label = 'sample bar 1', xerr = errors)
# plt.barh(mid_vals-1, counts2, facecolor = 'aquamarine', align = 'center', height = bar_width, label = 'sample bar 1', xerr = errors)
plt.barh(mid_vals, counts2, left = counts1, facecolor = 'aquamarine', align = 'center', height = bar_width, label = 'sample bar 1', xerr = errors)
plt.barh(mid_vals, counts3, left = counts1+counts2, facecolor = 'beige', align = 'center', height = bar_width, label = 'sample bar 1', xerr = errors)
plt.yticks(mid_vals)


# plt.xticks(mid_vals)
# plt.xticks(mid_vals+bar_width, groups, rotation = 'vertical')
plt.xlabel('values')
plt.ylabel('Count/Fraction')
plt.title('simple bar chart')
plt.grid()
plt.legend()

plt.show()