import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(languages, popularity, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

# Display values on bars
for i, value in enumerate(popularity):
    plt.text(i, value + 0.3, str(value), ha='center')

plt.show()
