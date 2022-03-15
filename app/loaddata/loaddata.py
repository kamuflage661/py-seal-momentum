import pandas as pd
import datetime
import time
import io
import os

#convert stock_names.txt to stock_names.csv

#For accessing the file in a folder contained in the current folder
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileInput = os.path.join(fileDir, 'data/stock_names.txt')
fileOutput = os.path.join(fileDir, 'data/tickers.csv')

read_file = pd.read_csv(fileInput, delim_whitespace=True)
read_file["<TICKER>"] = read_file["<TICKER>"].astype(str).str.casefold()

read_file.to_csv(fileOutput, index=True)