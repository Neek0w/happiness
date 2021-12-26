import pandas as pd

data = pd.read_csv('./dataSet/hapinness/2019.csv')

print(data.dropna(axis=0))
