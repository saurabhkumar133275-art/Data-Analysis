import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("HistoricalPrices.csv")
df=df.rename(columns={' Open':'Open',' High':'High',' Low':'Low',' Close':'Close'})
df['Date']=pd.to_datetime(df['Date'])
df=df.sort_values(by='Date')

dates=df['Date']
closing_price=df['Close']

plt.plot(dates,closing_price,linewidth=3,linestyle='solid')
plt.plot(dates, closing_price, linestyle='dotted')
plt.plot(dates, closing_price, linestyle='dashed')
plt.plot(dates, closing_price, linestyle='dashdot')
plt.show()
          
