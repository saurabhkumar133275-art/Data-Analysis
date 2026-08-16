import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(languages, popularity, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

# Attach text labels above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height + 0.3,
             f'{height:.1f}',
             ha='center',
             va='bottom')

plt.show()
