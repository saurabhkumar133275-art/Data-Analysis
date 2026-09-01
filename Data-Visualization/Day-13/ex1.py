import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.head())

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='total_bill', bins=20, kde=True, color='skyblue', edgecolor='black')

plt.title('Distribution of Total Bills (Seaborn)', fontsize=14)
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Count / Frequency', fontsize=12)
plt.show()
