import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

monthList = df['month_number']
faceCreamSalesData = df['facecream']
faceWashSalesData = df['facewash']

barWidth = 0.2

x = np.arange(len(monthList))

plt.bar(x, faceCreamSalesData,
        width=barWidth,
        label='Face Cream Sales Data')

plt.bar(x + barWidth, faceWashSalesData,
        width=barWidth,
        label='Face Wash Sales Data')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Face Cream and Face Wash Sales Data')

plt.xticks(x + barWidth/2, monthList)
plt.grid(True, linestyle='--')

plt.legend(loc='upper left')
plt.show()
