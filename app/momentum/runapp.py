from tqdm import tqdm
import os

for i in tqdm(range(1)):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileInput = os.path.join(fileDir, 'app/momentum/backtest.py')
    os.system('python '+ fileInput)
