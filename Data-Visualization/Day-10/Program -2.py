import matplotlib.pyplot as plt
import seaborn as sns

data = [44, 45, 40, 41, 39]
labels = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5']

colors = sns.color_palette("bright")

plt.figure(figsize=(7,7))

plt.pie(
    data,
    labels=labels,
    colors=colors,
    autopct='%.0f%%'
)

plt.title("Students in Different Classes")
plt.axis('equal')
plt.show()
