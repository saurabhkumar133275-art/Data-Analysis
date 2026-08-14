import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv("company_sales_data.csv")

# Get month number and total profit
monthList = data['month_number']
profitList = data['total_profit']

# Plot line chart
plt.plot(monthList,
         profitList,
         color='red',
         linestyle='dotted',
         linewidth=3,
         marker='o',
         markerfacecolor='red',
         label='Profit data of last year')

# Labels and title
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.title("Company Sales Data")

# Show legend at lower right
plt.legend(loc='lower right')

# Show month numbers on x-axis
plt.xticks(monthList)

plt.show()
