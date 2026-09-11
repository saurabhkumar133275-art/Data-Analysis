import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("D:/BCA_5D/Data_visu_7352/Ex_2/company_sales_data (1).csv")

salesData = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = ['FaceCream', 'FaceWash', 'ToothPaste',
          'BathingSoap', 'Shampoo', 'Moisturizer']

plt.pie(salesData,
        labels=labels,
        autopct='%1.1f%%')

plt.title('Sales data')

plt.legend(loc='lower right')

plt.show()
