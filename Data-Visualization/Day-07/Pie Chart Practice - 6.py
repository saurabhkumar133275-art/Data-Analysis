import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
colors = ["black", "hotpink", "blue", "#4CAF50"]

plt.pie(y, labels=labels, colors=colors)
plt.show()
