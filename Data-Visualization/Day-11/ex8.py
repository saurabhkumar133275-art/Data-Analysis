import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("HistoricalPrices.csv")
df=df.rename(columns={' Open':'Open',' High':'High',' Low':'Low',' Close':'Close'})
df['Date']=pd.to_datetime(df['Date'])
df=df.sort_values(by='Date')
df['High_minus_Low']=df['High']-df['Low']

dates=df['Date']
closing_price=df['Close']

fig, ax1 = plt.subplots()
ax1.plot(df['Date'], df['Close'], color='blue', label='Close Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Closing Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
print(df.head())
ax2 = ax1.twinx()
ax2.plot(df['Date'], df['High_minus_Low'], color='green', label='High - Low')
ax2.set_ylabel('High minus Low', color='green')
ax2.tick_params(axis='y', labelcolor='green') 
plt.title('DJIA Open and Close Prices')
plt.show()
         
