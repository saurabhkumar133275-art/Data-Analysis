import matplotlib.pyplot as plt
import seaborn as sns

data = [35, 25, 20, 15, 5]
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']

sns.set_theme(style="whitegrid", font_scale=1.1)

colors = sns.color_palette("pastel")

plt.figure(figsize=(8,6))

plt.pie(
    data,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops={
        'edgecolor': 'white',
        'linewidth': 2
    }
)

plt.title("Proportion Distribution Using Matplotlib & Seaborn")
plt.axis('equal')
plt.show()
