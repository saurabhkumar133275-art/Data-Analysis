import matplotlib.pyplot as plt
import seaborn as sns

data = [44, 45, 40, 41, 39]
labels = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5']

explode = [0, 0.1, 0, 0, 0]

colors = sns.color_palette("dark")

plt.figure(figsize=(7,7))

plt.pie(
    data,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%.0f%%'
)

plt.title("Students Distribution")
plt.axis('equal')
plt.show()
