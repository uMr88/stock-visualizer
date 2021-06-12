import time
import datetime
import pandas as pd

import matplotlib.pyplot as plt

ticker = '%5ENSEI'
period1 = int(time.mktime(datetime.datetime(2011, 6, 7, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 6, 7, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
print(df.shape)


df=(df[df['Open'] > 1])


print(df.shape)
df.to_csv('NSE1.csv')

df1 = pd.read_csv('NSE1.csv')


print(df1.Gross.value_counts())
df2 = df1.value_counts(df1.Gross).to_frame().reset_index()

df2.columns = ['values','Count']


df2.plot.bar()
plt.show()
