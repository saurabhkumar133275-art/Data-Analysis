import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("company_sales_data.csv")

# Get data
monthList = data['month_number']
profitList = data['total_profit']

# Create line plot
plt.plot(monthList, profitList)

# Labels
plt.xlabel("Month Number")
plt.ylabel("Total profit")
plt.title("Company Profit per Month")

plt.show()
