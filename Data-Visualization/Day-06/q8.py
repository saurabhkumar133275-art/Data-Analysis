import matplotlib.pyplot as plt
import numpy as np

# Sample data
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)

# Number of groups
groups = np.arange(len(means_men))

# Width of each bar
bar_width = 0.35  

# Plot bars
plt.bar(groups, means_men, bar_width, label='Men', color='blue')
plt.bar(groups + bar_width, means_women, bar_width, label='Women', color='pink')

# Labels and title
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(groups + bar_width / 2, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

# Show plot
plt.show()
