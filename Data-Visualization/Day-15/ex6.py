import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

monthList = df['month_number']
bathingSoapSalesData = df['bathingsoap']

plt.bar(monthList, bathingSoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Bathing Soap Sales Data')

plt.xticks(monthList)
plt.grid(True, linestyle='--')

plt.savefig('sales_data_of_bathing_soap.png',
            dpi=150,
            bbox_inches='tight')

plt.show()
