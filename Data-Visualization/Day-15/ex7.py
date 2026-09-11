import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

profitList = df['total_profit']

profit_range = [150000, 175000, 200000,
                225000, 250000,
                300000, 350000]

plt.hist(profitList,
         bins=profit_range,
         label='Profit data')

plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.title('Profit data')
plt.legend(loc='upper left')

plt.show()
