import backtrader as bt

class SingleStockStrategy(bt.Strategy):
    def __init__(self):
        print('call init')
    def next(self):
        print('call next')