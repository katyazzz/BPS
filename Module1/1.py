import pandas as pd
df = pd.read_csv('trades.txt', names = ['Company', 'Price', 'Amount', 'DateTime'])

mask1 = (df['DateTime'] > '2019-01-30 07:00:00') & (df['DateTime'] <= '2019-01-31 03:00:00')
df1=df.loc[mask1]
mask2=(df['DateTime'] > '2019-01-31 07:00:00') & (df['DateTime'] <= '2019-02-01 03:00:00')
df2=df.loc[mask2]
df = pd.concat([df1,df2])
print(df)
df['DateTime'] =pd.to_datetime(df['DateTime'])
df.reset_index()
df=df.set_index('DateTime')
sber_df = df[df['Company'] == 'SBER']
amzn_df = df[df['Company'] == 'AMZN']
aapl_df = df[df['Company'] == 'AAPL']

sberdp30 = sber_df['Price'].resample('30Min').ohlc()
sberdp5 = sber_df['Price']. resample('5Min'). ohlc()
sberdp240= sber_df['Price'].resample('240Min'). ohlc()
aapldp30 = aapl_df['Price'].resample('30Min').ohlc()
aapldp5 = aapl_df['Price']. resample('5Min'). ohlc()
aapldp240= aapl_df['Price'].resample('240Min'). ohlc()
amzndp30 = amzn_df['Price'].resample('30Min').ohlc()
amzndp5 = amzn_df['Price']. resample('5Min'). ohlc()
amzndp240= amzn_df['Price'].resample('240Min'). ohlc()

sberdp30['Company']='SBER'
aapldp30['Company']='AAPL'
amzndp30['Company']='AMZN'
sberdp5['Company']='SBER'
aapldp5['Company']='AAPL'
amzndp5['Company']='AMZN'
sberdp240['Company']='SBER'
aapldp240['Company']='AAPL'
amzndp240['Company']='AMZN'
pc30 = pd.concat([sberdp30, aapldp30, amzndp30])
pc30.sort_index(inplace=True)
pc5 = pd.concat([sberdp5, aapldp5, amzndp5])
pc5.sort_index(inplace=True)
pc240 = pd.concat([sberdp240, aapldp240, amzndp240])
pc240.sort_index(inplace=True)
dfnew = ['Company', 'open', 'high', 'low', 'close']
pc30 = pc30[dfnew]
pc240 = pc240[dfnew]
pc5 = pc5[dfnew]
print(pc5.to_csv)
print(pc30.to_csv)
print(pc240.to_csv)
