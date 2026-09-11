import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

monthList = df['month_number']
toothpasteSalesData = df['toothpaste']

plt.scatter(monthList,
            toothpasteSalesData,
            label='Tooth paste Sales Data')

plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Tooth paste Sales Data')
plt.xticks(monthList)
plt.grid(True, linestyle='--')
plt.legend(loc='upper left')
plt.show()
