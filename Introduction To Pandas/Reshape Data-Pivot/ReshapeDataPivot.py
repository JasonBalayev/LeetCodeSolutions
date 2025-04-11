import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')

#QED
#Problem 2889 (Easy) - Jason Balayev (python)


