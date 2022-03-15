import backtrader as bt
import pandas as pd
import datetime as datetime
from custom_strategy import CustomStrategy

cerebro = bt.Cerebro(stdstats=False)
cerebro.broker.set_coc(True)

spy = pd.read_csv(f"data/wse indices/wig20.txt",
                  parse_dates=['<DATE>'],
                  index_col=['<DATE>'])

spy = spy.rename(columns={
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


spy = spy[spy.index.to_series().between('2020-02-16', '2022-02-18')]

cerebro.adddata(bt.feeds.PandasData(dataname=spy, plot=False))  # add WIG Index


tickers = pd.read_csv('data/tickers.csv')["<TICKER>"].tolist()

for ticker in tickers:
    df = pd.read_csv(f"data/wse stocks/{ticker}.txt",
                     parse_dates=True,
                     index_col='<DATE>')
    if len(df) > 100:  # data must be long enough to compute 100 day SMA
        df = df.rename(columns={
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

        df = df[df.index.to_series().between('2020-02-16', '2022-02-18')]

        cerebro.adddata(bt.feeds.PandasData(dataname=df, plot=False))

cerebro.addobserver(bt.observers.Value)
cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0)
cerebro.addanalyzer(bt.analyzers.Returns)
cerebro.addanalyzer(bt.analyzers.DrawDown)
cerebro.addstrategy(CustomStrategy)
results = cerebro.run()


cerebro.plot(iplot=False)[0][0]
print(
    f"Sharpe: {results[0].analyzers.sharperatio.get_analysis()['sharperatio']:.3f}")
print(
    f"Norm. Annual Return: {results[0].analyzers.returns.get_analysis()['rnorm100']:.2f}%")
print(
    f"Max Drawdown: {results[0].analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")