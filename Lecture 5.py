# Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame opening stock price / three dates
opening_prices = [100, 101, 99]
dates = ['2021-01-04', '2021-01-05','2021-01-06']
data = {'Opening Price': opening_prices}
df = pd.DataFrame(data, index=dates)
print(df)

# DataFrame Price / Volume / High / Low
import pandas as pd
prices = [100 , 101 , 102 ]
volumes = [200 , 210 , 220 ]
dates = ['2021-01-04', '2021-01-05','2021-01-06']
data = {'Prices': prices, 'Volumes': volumes }
df = pd.DataFrame(data, index=dates)
df['High'] = df['Prices'].max()
df['Low'] = df['Prices'].min()
print(df)

# Transforming NumPy array to DataFrame Closing Price
closing_prices = np.array([100, 101, 99, 102, 101, 103, 104])
df = pd.DataFrame({'Closing Price': closing_prices})
df['Price Change (pct)'] = df['Closing Price'].pct_change() * 100
print(df)

# Transforming NumPy array to DataFrame Volume / Average Trade Size
volume_trades = np.array([10000, 15000, 12000, 18000, 9000])
average_trade_size = np.array([500, 600, 450, 700, 550])
data = {'Volume': volume_trades,'Average Trade Size': average_trade_size}
df = pd.DataFrame(data)
df['Volume'] = df['Volume'].astype(int)
df['Average Trade Size'] = df['Average Trade Size'].astype(float)
print(df)

# DataFrame Date / Close / Volume / Day of the week
start_date = '2023-10-01'
end_date = '2023-10-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='B')
closing_prices = []
volumes = []
for date in date_range:
    closing_prices.append(100 + date.day - 1)
    volumes.append(200 + date.day - 1)
data = {'Date': date_range, 'Close': closing_prices, 'Volume': volumes}
df = pd.DataFrame(data)
df['Day of the Week'] = df['Date'].dt.day_name()
print(df)
mondays = df.loc[df['Date'].dt.weekday == 0]
average = mondays['Volume'].mean()
print(mondays)
print("Average Volume for Mondays:", average)

# DataFrame with closing prices / Mean & Median / Max and Min / day with highest and lowest closing prices
data = {'Date': pd.date_range(start='2023-10-01', periods=7, freq='D'),
        'Close': [100, 102, 105, 103, 108, 110, 107]}
df = pd.DataFrame(data)
mean = df['Close'].mean()
median = df['Close'].median()
max = df['Close'].max()
min = df['Close'].min()
day_max = df.loc[df['Close'] == max]['Date'].values[0]
day_min = df.loc[df['Close'] == min]['Date'].values[0]
print(mean,median,max,min,day_max,day_min)

# Line plot of closing prices
data = {'Date': pd.date_range(start='2023-10-01', periods=7, freq='D'),
        'Close': [100, 102, 105, 103, 108, 110, 107]}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-')
plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()

# Bar plot of closing prices / day with the highest closing price
data = {'Date': pd.date_range(start='2023-10-01', periods=7, freq='D'),
        'Close': [100, 102, 105, 103, 108, 110, 107]}
df = pd.DataFrame(data)
max_price = df['Close'].max()
day_with_max_price = df.loc[df['Close'] == max_price]['Date'].values[0]

plt.figure(figsize=(10, 6))
bars = plt.bar(df['Date'], df['Close'], color='blue')
for bar in bars:
    if bar.get_height() == max_price:
        bar.set_color('red')

plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()

# Pandas Series / Daily return / Moving average / Plot original closing price
stock_prices = pd.Series(np.random.rand(10) * 100, name="Stock Prices")
daily_returns = stock_prices.pct_change().dropna() * 100
moving_average = stock_prices.rolling(window=3).mean()
plt.figure(figsize=(10, 6))
plt.plot(stock_prices, label="Closing Prices", marker='o')
plt.plot(moving_average, label="3-Day Moving Average", linestyle='--', color='orange', marker='o')
plt.title("Stock Prices and 3-Day Moving Average")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()
plt.show()

# DataFrame / Average trading volume per day / day with the highest volume
## Price column / Total Traded value / highest total traded value
data = {
    'Symbol': ['AAPL', 'MSFT', 'GOOG', 'AAPL', 'GOOG', 'MSFT'],
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-02'],
    'Volume': [100, 150, 200, 90, 120, 160]}
trades = pd.DataFrame(data)
average_volume_per_day = trades.groupby('Date')['Volume'].mean()
max_average_volume_day = average_volume_per_day.idxmax()
max_average_volume = average_volume_per_day.max()
print(average_volume_per_day)
print(f"\nThe day with the highest average trading volume is {max_average_volume_day} with an average volume of {max_average_volume}.\n")

trades['Price'] = [150, 200, 250, 160, 210, 180]
trades['Total Traded Value'] = trades['Volume'] * trades['Price']
total_traded_value_per_symbol = trades.groupby('Symbol')['Total Traded Value'].sum()
max_total_traded_value_stock = total_traded_value_per_symbol.idxmax()
max_total_traded_value = total_traded_value_per_symbol.max()
print(total_traded_value_per_symbol)
print(f"\nThe stock with the highest total traded value is {max_total_traded_value_stock} with a total traded value of {max_total_traded_value}.\n")

# DataFrame & conditions
data = {
    'Symbol': ['AAPL', 'MSFT', 'AAPL', 'GOOG', 'MSFT'],
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'Close': [150, 250, 145, 1000, 255],
    'Volume': [100, 300, 90, 150, 350]}
stocks = pd.DataFrame(data)
selected_rows_exercise_1 = stocks[(stocks['Symbol'] == 'AAPL') & (stocks['Close'] > 140)]
print(selected_rows_exercise_1)
print("\n")
stocks['Volume Change'] = stocks['Volume'].diff().fillna(0)
median_close_price = stocks['Close'].median()
selected_complex_rows_exercise_2 = stocks[(stocks['Volume Change'] > 50) & (stocks['Close'] < median_close_price)]
print(selected_complex_rows_exercise_2)

# Two DataFrames closing & opening prices for a stock over the same period
# Daily price movement / align dividend payout
closing_prices = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Close': [150, 155, 160]})
opening_prices = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Open': [145, 152, 158]})
stock_prices = pd.concat([closing_prices, opening_prices['Open']], axis=1)
stock_prices['Daily Movement'] = stock_prices['Close'] - stock_prices['Open']
print("Concatenated Stock Prices with Daily Movement:")
print(stock_prices)
print("\n")

df_dividends = pd.DataFrame({
    'Symbol': ['AAPL', 'GOOG', 'MSFT'],
    'Ex Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Dividend': [2.0, 1.5, 1.8]
})

df_earnings = pd.DataFrame({
    'Symbol': ['AAPL', 'GOOG', 'MSFT', 'AMZN'],
    'Report Date': ['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-02'],
    'Earnings': [10.5, 8.0, 12.2, 9.7]})
merged_df = pd.merge(df_dividends, df_earnings, on='Symbol', how='outer')
dividends_no_earnings = merged_df[merged_df['Dividend'].notna() & merged_df['Earnings'].isna()]
earnings_no_dividends = merged_df[merged_df['Dividend'].isna() & merged_df['Earnings'].notna()]
print("Symbols with Dividends but No Earnings:")
print(dividends_no_earnings)
print("\nSymbols with Earnings but No Dividends:")
print(earnings_no_dividends)

import pandas as pd

# Exercise 1
# Assuming you have two DataFrames 'df_prices' and 'df_volumes'
df_prices = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Stock': ['AAPL', 'GOOG', 'MSFT'],
    'Close': [150, 160, 140]
})

df_volumes = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Stock': ['AAPL', 'GOOG', 'MSFT'],
    'Volume': [100, 120, 80]
})

# Right join
result_right_join = pd.merge(df_prices, df_volumes, on=['Date', 'Stock'], how='right')

print("Result of Right Join:")
print(result_right_join)
print("\nExplanation:")
print("A right join includes all the rows from the right DataFrame ('df_volumes') and the matching rows from the left DataFrame ('df_prices').")
print("If there is no match in the left DataFrame for a row in the right DataFrame, the result will contain NaN values in the columns from the left DataFrame.")
print("This type of join might be used in financial analysis when you are primarily interested in the information from the right DataFrame (e.g., volume data), and you want to include corresponding information from the left DataFrame where available (e.g., closing prices).")

# Outer join
result_outer_join = pd.merge(df_prices, df_volumes, on=['Date', 'Stock'], how='outer')

print("\nResult of Outer Join:")
print(result_outer_join)
print("\nBenefits and Drawbacks of Outer Join:")
print("Benefits: An outer join includes all rows from both DataFrames, filling in NaN values where there is no match.")
print("Drawbacks: The drawback is that the resulting DataFrame may have a large number of NaN values, especially if there are many non-matching rows in either DataFrame. This can complicate analysis and interpretation.")

# Exercise 2
# Assuming you have two DataFrames 'df_dividends' and 'df_stock_splits'
df_dividends = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Stock': ['AAPL', 'GOOG', 'MSFT'],
    'Dividend': [2.0, 1.5, 1.8]
})

df_stock_splits = pd.DataFrame({
    'Date': ['2023-01-02', '2023-01-03'],
    'Stock': ['GOOG', 'MSFT'],
    'Split Ratio': [2, 3]
})

# Inner join to find dates and stocks where both dividends were issued and a stock split occurred
result_inner_join = pd.merge(df_dividends, df_stock_splits, on=['Date', 'Stock'], how='inner')

print("Result of Inner Join:")
print(result_inner_join)
print("\nExplanation:")
print("An inner join includes only the rows where there are matching values in both DataFrames.")
print("In this case, it will include only the dates and stocks where both dividends were issued and a stock split occurred.")

# Outer join to provide a more comprehensive view of corporate actions over a period
result_outer_join = pd.merge(df_dividends, df_stock_splits, on=['Date', 'Stock'], how='outer')

print("\nResult of Outer Join:")
print(result_outer_join)
print("\nAnalysis of Outer Join:")
print("An outer join provides a more comprehensive view by including all rows from both DataFrames.")
print("This can be useful for understanding the full timeline of corporate actions, including dates where only dividends, only stock splits, or both occurred.")
