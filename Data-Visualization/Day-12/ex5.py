import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

axes[0].hist(data1, bins=30, color='Yellow', edgecolor='black')
axes[0].set_title('Histogram 1')
axes[1].hist(data2, bins=30, color='Pink', edgecolor='black')
axes[1].set_title('Histogram 2')

for ax in axes:
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')

plt.tight_layout()
plt.show()
