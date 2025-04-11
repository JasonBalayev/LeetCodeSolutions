import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

#QED
#Problem 2888 (Easy) - Jason Balayev (python)



