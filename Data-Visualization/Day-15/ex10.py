import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20)
y = np.random.rand(20)

colors = ['b', 'r', 'y', 'c'] * 5
sizes = 1000 * np.random.rand(20)

plt.scatter(x, y,
            s=sizes,
            c=colors,
            alpha=0.8)

plt.xlabel('X')
plt.ylabel('Y')

plt.show()
