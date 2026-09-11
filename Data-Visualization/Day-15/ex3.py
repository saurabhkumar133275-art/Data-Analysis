import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

monthList = df['month_number']

plt.plot(monthList, df['facecream'],
         label='Face cream Sales Data',
         marker='o', linewidth=3)

plt.plot(monthList, df['facewash'],
         label='Face Wash Sales Data',
         marker='o', linewidth=3)

plt.plot(monthList, df['toothpaste'],
         label='ToothPaste Sales Data',
         marker='o', linewidth=3)

plt.plot(monthList, df['bathingsoap'],
         label='BathingSoap Sales Data',
         marker='o', linewidth=3)

plt.plot(monthList, df['shampoo'],
         label='Shampoo Sales Data',
         marker='o', linewidth=3)

plt.plot(monthList, df['moisturizer'],
         label='Moisturizer Sales Data',
         marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')

plt.xticks(monthList)
plt.legend(loc='upper left')

plt.show()
