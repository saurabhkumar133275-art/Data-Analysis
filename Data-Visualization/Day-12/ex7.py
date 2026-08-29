import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = 2 * x + np.random.normal(size=1000)

plt.hexbin(x, y, gridsize=30, cmap='Blues')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram (Hexbin Plot)')
plt.colorbar(label='Counts')
plt.show()
 
