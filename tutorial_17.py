import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')

lim1 = 1
lim2 = 10
N = 11

years = np.linspace(2000, 2010, N, dtype = np.int64)
expense1 = np.random.randint(lim1, lim2, N)
expense2 = np.random.randint(lim1, lim2, N)
expense3 = np.random.randint(lim1, lim2, N)
expense4 = np.random.randint(lim1, lim2, N)
expense5 = np.random.randint(lim1, lim2, N)
expenses = [expense1, expense2, expense3, expense4, expense5] 

labels = ['Education', 'Medication', 'Charity', 'Infraestructure', 'Defence']
colors = ['blue', 'green', 'red', 'black', 'yellow']

plt.stackplot(years, expenses, colors = colors, labels = labels)

plt.xlabel('Years')  
plt.ylabel('Accumulated expenses')
plt.title('Stacked plot: expenses in {} city for 11 years in {} {}'.format('Coimbatore', 'Million', 'Rupees'))
plt.grid()
plt.legend()
plt.show()