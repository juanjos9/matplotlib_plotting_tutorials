import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('default')

distritos = [
    'Arch Linux', 'Ubuntu', 'Debian',
    'Fedora', 'Linux Mint', 'Xubuntu',
    'Kubuntu', 'Gentoo', 'OpenSUSE', 'Other'
]

colors = [
    'blue', 'orange', 'red', 'purple', 'green',
    'chocolate', 'beige', 'cyan', 'magenta', 'grey'
]

# Slice data
users = np.array([881, 697, 308, 262, 209, 117, 99, 97, 58, 366])

# Slice cut array
explodes = np.zeros(10)
explodes[1] = 0.1

 
# plt.pie(users, labels = distritos, colors = colors, startangle= 90, shadow=True,
# explode= explodes, radius= 1.0, autopct='%2.2f%%', pctdistance=0.8, 
# labeldistance=1.5, frame = False)

plt.title('Piechart: Linux Distro Popularity in a community')

plt.show()
