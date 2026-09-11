import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

profitList = df['total_profit'].tolist()
months = df['month_number'].tolist()

plt.plot(months, profitList)
plt.xlabel('Month number')
plt.ylabel('Profit in number')
plt.title('Company profit per month')
plt.xticks(months)

plt.show()


 
