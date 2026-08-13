import pandas as pd

data = pd.read_csv(r"D:\Data_visu_7352\tips.csv")

print(data.head())
print(data.info())
print(data.describe())
