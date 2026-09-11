import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

monthList = df['month_number']

plt.subplot(2, 1, 1)
plt.plot(monthList, df['bathingsoap'],
         color='black', marker='o')
plt.title('Sales data of Bathingsoap')

plt.subplot(2, 1, 2)
plt.plot(monthList, df['facewash'],
         color='red', marker='o')
plt.title('Sales data of Facewash')
plt.xlabel('Month Number')
plt.tight_layout()
plt.show()
