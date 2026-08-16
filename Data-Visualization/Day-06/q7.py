import matplotlib.pyplot as plt
import numpy as np

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Set positions of bars
x_pos = np.arange(len(languages))

# Set width of each bar
bar_width = 0.6

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(x_pos, popularity, width=bar_width, color='skyblue', edgecolor='black')

# Set custom labels on x-axis
plt.xticks(x_pos, languages)

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

# Add values above bars
for i, value in enumerate(popularity):
    plt.text(x_pos[i], value + 0.3, f'{value:.1f}', ha='center')

plt.show()
