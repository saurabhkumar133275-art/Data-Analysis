import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.head())

plt.figure(figsize=(8, 5))
plt.hist(df['total_bill'], bins=15, color='salmon', edgecolor='black', alpha=0.7)
plt.title('Distribution of Total Bills (Matplotlib)', fontsize=14)
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


