import backtrader as bt
import pandas as pd

import strategysinglestock as strategysinglestock

def runBacktests(data: pd.DataFrame ):
    cerebro = bt.Cerebro(stdstats=False)
    cerebro.broker.set_coc(True)
    cerebro.addstrategy(strategysinglestock.SingleStockStrategy)
    cerebro.adddata(bt.feeds.PandasData(dataname=data, plot=True))
    cerebro.broker.setcash(5000)
    results = cerebro.run()

    cerebro.plot()
    #cerebro.plot(iplot=False)[0][0]