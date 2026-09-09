import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])

plt.scatter(x, y, marker='^', color='magenta', s=100, alpha=0.7)
plt.title("Scatter Plot with Triangle Markers")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
