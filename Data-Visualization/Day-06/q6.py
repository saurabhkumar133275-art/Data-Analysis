import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Specify bar positions
x_pos = [0, 1, 2, 3, 4, 5]

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(x_pos, popularity, color='skyblue', edgecolor='black')

# Set labels at specified positions
plt.xticks(x_pos, languages)

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

# Add values above bars
for i, value in enumerate(popularity):
    plt.text(x_pos[i], value + 0.3, str(value), ha='center')

plt.show()
