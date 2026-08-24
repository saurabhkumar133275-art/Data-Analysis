import pandas as pd
import matplotlib.pyplot as plt

courses = [164, 127, 31, 31, 12, 11]
labels = ['Python', 'R', 'SQL', 'Power BI', 'Excel', 'ChatGPT']

dictionary = {
    'courses': courses,
    'labels': labels
}

python_pie_chart_df = pd.DataFrame(dictionary)

plt.figure(figsize=(6, 6))
plt.pie(x=python_pie_chart_df['courses'])

plt.legend(
    labels=python_pie_chart_df['labels'],
    title="Technologies",
    loc="upper right"
)

plt.title("Course Distribution")

plt.show()
