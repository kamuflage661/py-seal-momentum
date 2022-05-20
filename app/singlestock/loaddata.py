import pandas as pd

def readTicker(ticker) -> pd.DataFrame:
    tickerData = pd.read_csv(f"data/wse stocks/{ticker}.txt", parse_dates=True, index_col='<DATE>')
    return prepareData(tickerData,'2017-02-16', '2022-02-18')

def prepareData(data : pd.DataFrame, dateFrom : str, dateTo : str) -> pd.DataFrame:
    data = data.rename(
        columns={
        "<TICKER>": "ticker",
        "<PER>": "per",
        "<TIME>": "time",
        "<OPEN>": "open",
        "<HIGH>": "high",
        "<LOW>": "low",
        "<CLOSE>": "close",
        "<VOL>": "volume",
        "<OPENINT>": "openint"
        })
    data.index.name = "date"    
    return data[data.index.to_series().between(dateFrom, dateTo)]
