import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'a': [2, 4, 6, 8, 10],
    'b': [4, 2, 4, 2, 4],
    'c': [8, 3, 7, 6, 4],
    'd': [5, 4, 4, 4, 3],
    'e': [7, 2, 7, 8, 3],
    'f': [6, 6, 8, 6, 2]   # Added last column from your sample row
}

df = pd.DataFrame(data)

# Plot bar chart
df.plot(kind='bar')

# Labels and title
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Bar Plot from DataFrame')
plt.legend(title='Columns')

# Show plot
plt.show()
