import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(50, 150, 100)
y = np.random.randint(50, 150, 100)

colors = np.random.rand(100)
sizes = 20 * np.random.randint(10, 100, 100)

plt.scatter(x, y, c=colors, s=sizes, cmap='viridis', alpha=0.7)
plt.colorbar(label='Color Scale')
plt.title("Scatter Plot with Colormap and Colorbar")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
