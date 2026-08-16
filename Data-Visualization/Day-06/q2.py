import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create horizontal bar chart
plt.figure(figsize=(8, 5))
plt.barh(languages, popularity, color='lightgreen', edgecolor='black')

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')

# Display values on bars
for i, value in enumerate(popularity):
    plt.text(value + 0.3, i, str(value), va='center')

plt.show()
