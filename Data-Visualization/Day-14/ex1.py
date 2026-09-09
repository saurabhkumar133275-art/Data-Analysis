import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
y = np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])

# Scatter Plot
plt.scatter(x, y)

# Title and Labels
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Show Plot
plt.show()
