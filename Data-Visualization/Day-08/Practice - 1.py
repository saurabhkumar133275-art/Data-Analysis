import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
penguins = sns.load_dataset('penguins')

# Count each penguin species
species_counts = penguins['species'].value_counts()

# Create pie chart
plt.figure(figsize=(5,5))
plt.pie(species_counts, labels=species_counts.index)

plt.title("Penguin Species Distribution")
plt.show()
