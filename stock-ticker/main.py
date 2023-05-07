import threading
import yfinance as yf
import pandas as pd
import time
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def retrieve_stock_data():
    symbols = ['AAPL', 'MSFT', 'GOOGL']
    
    while True:
        data = yf.download(tickers=symbols, period='1d', interval='5m')
        for index, row in data.iterrows():
            for symbol in symbols:
                date = index
                price = row['Close'][symbol]
                print(f"Symbol: {symbol} - Date: {date} - Price: {price}")
                # redis_client.set(symbol, str(price))
            time.sleep(10)  # Sleep for 1 minute

        # Sleep for a specific duration before retrieving the next data

# Start the stock data retrieval in a separate thread
thread = threading.Thread(target=retrieve_stock_data)
thread.start()
