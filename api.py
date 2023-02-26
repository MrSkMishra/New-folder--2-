import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(stock_list):
   
    url = 'https://api.nsepy.xyz/api/quote'
    stock_data = {}
    for stock in stock_list:
        params = {'symbol': stock, 'series': 'EQ'}
        response = requests.get(url, params=params)
        data = response.json()['data']
        stock_data[stock] = data
    return stock_data


def plot_stock_data(stock_data):
    
    fig, ax = plt.subplots()
    for stock in stock_data:
        data = stock_data[stock]
        dates = [x['Date'] for x in data]
        close_values = [x['Close'] for x in data]
        ax.plot(dates, close_values, label=stock)
    ax.set_xticks(ax.get_xticks()[::30])
    ax.legend()
    ax.set_title('Closing Values of Stocks')
    plt.show()


def concat_stock_data(stock_data):
    
    stock_data_list = []
    for stock in stock_data:
        data = stock_data[stock]
        df = pd.DataFrame(data)
        df['Stock'] = stock
        stock_data_list.append(df)
    table_value = pd.concat(stock_data_list, axis=0, ignore_index=True)
    table_value = table_value.pivot(index='Date', columns='Stock', values='Close')
    return table_value


stock_list = ['SBIN', 'ASIANPAINT', 'AXISBANK']
stock_data = fetch_stock_data(stock_list)

plot_stock_data(stock_data)

table_value = concat_stock_data(stock_data)
print(table_value)