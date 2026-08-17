import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode = [0.2, 0, 0, 0]

plt.pie(y, labels=labels, explode=explode)
plt.show()
