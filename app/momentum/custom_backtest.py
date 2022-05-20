import backtrader as bt
import pandas as pd
import datetime as datetime
from custom_strategy import CustomStrategy

cerebro = bt.Cerebro(stdstats=False)
cerebro.broker.set_coc(True)

#define function to prepare data
def prepareData(data, dateFrom, dateTo):
    data = data.rename(columns={
        "<DATE>": "date",
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

    return data[data.index.to_series().between(dateFrom, dateTo)]

#prepare indicator
spy = pd.read_csv(f"data/wse indices/wig20.txt",
                  parse_dates=['<DATE>'],
                  index_col=['<DATE>'])

spy = prepareData(spy,'2020-02-16', '2022-02-18')

cerebro.adddata(bt.feeds.PandasData(dataname=spy, plot=False))  # add WIG Index

#prepare stock data
tickers = pd.read_csv('data/tickers.csv')["<TICKER>"].tolist()

for ticker in tickers:
    df = pd.read_csv(f"data/wse stocks/{ticker}.txt",
                     parse_dates=True,
                     index_col='<DATE>')
    if len(df) > 100:  # data must be long enough to compute 100 day SMA
        df = prepareData(df,'2020-02-16', '2022-02-18')

        cerebro.adddata(bt.feeds.PandasData(dataname=df, plot=False), name=ticker)


#set up
cerebro.addobserver(bt.observers.Value)
cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0)
cerebro.addanalyzer(bt.analyzers.Returns)
cerebro.addanalyzer(bt.analyzers.DrawDown)
cerebro.addstrategy(CustomStrategy)

cerebro.broker.setcash(10000)
cerebro.broker.setcommission(0.002)

#run strategy
results = cerebro.run()


cerebro.plot(iplot=False)[0][0]
print(
    f"Sharpe: {results[0].analyzers.sharperatio.get_analysis()['sharperatio']:.3f}")
print(
    f"Norm. Annual Return: {results[0].analyzers.returns.get_analysis()['rnorm100']:.2f}%")
print(
    f"Max Drawdown: {results[0].analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")