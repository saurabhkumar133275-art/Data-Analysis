import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)

plt.hist([data1, data2], bins=30, stacked=True, color=['cyan', 'Purple'], edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Stacked Histogram')
plt.legend(['Dataset 1', 'Dataset 2'])
plt.show()
