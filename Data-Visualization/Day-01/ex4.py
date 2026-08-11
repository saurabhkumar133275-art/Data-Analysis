import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6])  # custom x-values
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(xpoints, ypoints, marker='o')  # adds markers
plt.show()
