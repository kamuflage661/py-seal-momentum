from datetime import datetime
import numpy as np
import pandas as pd


stock1 = {'2017-02-01': 22.0, '2017-02-02': 21.00, '2017-02-10': 30.1, '2017-05-10': 130.1}
stock2 = {'2017-02-01': 2.0, '2017-02-02': 121.00, '2015-02-02': 11.33, '2017-02-10': 50.1}

stock1Series = pd.Series(data=stock1, name='stock1')
stock2Series = pd.Series(data=stock2, name='stock2')


concatedDataFrame = pd.concat([stock1Series, stock2Series], axis=1)

concatedDataFrame = concatedDataFrame.rename(columns={"stock1":"name1", "stock2":"name2"})

print(concatedDataFrame)