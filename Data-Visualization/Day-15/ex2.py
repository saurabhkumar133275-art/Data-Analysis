import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

months = df['month_number']
profit = df['total_profit']

plt.plot(
    months,
    profit,
    linestyle='--',       
    color='red',          
    marker='o',           
    markerfacecolor='red',
    linewidth=3,
    label='Profit data of last year'
)
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Company Sales Data')
plt.xticks(months)
plt.legend(loc='lower right')
plt.show()
