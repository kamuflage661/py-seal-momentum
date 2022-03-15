from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

tickers = pd.read_csv(dir_path +"/testdata/tickers.csv")["<TICKER>"].tolist()

#create a list of series with name as ticker
allTickersData = [
    pd.read_csv(dir_path + f"/data/wse stocks/{ticker}.txt",
                index_col='<DATE>',
                parse_dates=True)['<CLOSE>'].rename(ticker) for ticker in tickers]

stocks = pd.concat(allTickersData, axis=1, sort=True)

print(stocks)