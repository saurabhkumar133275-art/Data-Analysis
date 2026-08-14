import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv("company_sales_data.csv")

monthList = data['month_number']

# Plot each product sales
plt.plot(monthList, data['facecream'], label='Face Cream Sales Data', marker='o')
plt.plot(monthList, data['facewash'], label='Face Wash Sales Data', marker='o')
plt.plot(monthList, data['toothpaste'], label='ToothPaste Sales Data', marker='o')
plt.plot(monthList, data['bathingsoap'], label='BathingSoap Sales Data', marker='o')
plt.plot(monthList, data['shampoo'], label='Shampoo Sales Data', marker='o')
plt.plot(monthList, data['moisturizer'], label='Moisturizer Sales Data', marker='o')

# Labels
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("Sales data")

# Show month numbers
plt.xticks(monthList)

# Legend
plt.legend(loc='upper left')

plt.show()
