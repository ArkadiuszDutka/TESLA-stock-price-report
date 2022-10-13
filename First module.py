# import of libraries
import pandas as pd
import matplotlib.pyplot as plt

# in code below we will indicate our source of information about stock price of TESLA
# for now I have only this solution, in near future I will like automated process
data = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1634093757&period2=1665629757&interval=1d&events=history&includeAdjustedClose=true')

# print(data)

# in code below we will change format in column 'Date' from object to datetime
data['Date'] = pd.to_datetime(data['Date'])

# data.info()

plt.figure(figsize=(16, 6))

plt.plot(data['Date'], data['Close'], color='blue', linewidth=2.5)
plt.xlim(data['Date'].min(), data['Date'].max())
plt.ylim(200, data['Close'].max()*1.05)
plt.xlabel('Date')
plt.ylabel('Close')
plt.title('Tesla, Inc. (TSLA)')


# plt.show()
# in code below we will save csv file to our project, file will be use in second module
plt.savefig('TSLA13102022.png')

print("It's done!")