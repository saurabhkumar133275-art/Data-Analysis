import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create bar chart with uniform color
plt.figure(figsize=(8, 5))
plt.bar(languages, popularity, color='blue')

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

plt.show()
