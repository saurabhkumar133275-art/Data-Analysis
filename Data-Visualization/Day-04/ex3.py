import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('D:/Data_visu_7352/Practice_1_7352/tips.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()
 
