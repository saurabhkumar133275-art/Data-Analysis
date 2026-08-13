import pandas as pd

data = pd.read_csv("tips.csv")

print(data.head())
print(data.info())
print(data.describe())
