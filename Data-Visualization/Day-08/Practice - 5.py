import pandas as pd
import matplotlib.pyplot as plt

courses = [164, 127, 31, 31, 12, 11]
labels = ['Python', 'R', 'SQL', 'Power BI', 'Excel', 'ChatGPT']

dictionary = {
    'courses': courses,
    'labels': labels
}

python_pie_chart_df = pd.DataFrame(dictionary)

datacamp_palette = [
    '#03ef62',
    '#06bdfc',
    '#ff6ea9',
    '#ff931e',
    '#ff5400',
    '#7933ff'
]

plt.figure(figsize=(6,6))
plt.pie(
    x=python_pie_chart_df['courses'],
    labels=python_pie_chart_df['labels'],
    colors=datacamp_palette,
    autopct='%1.1f%%'
)

plt.title("Course Distribution")
plt.show()
