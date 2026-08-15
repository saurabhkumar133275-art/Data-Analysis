import matplotlib.pyplot as plt
import numpy as np

# X-axis values (Categories)
x = np.array(["A", "B", "C", "D"])

# Y-axis values
y = np.array([3, 8, 1, 10])

# Create Bar Chart
plt.bar(x, y, color="red")

# Display the graph
plt.show()
