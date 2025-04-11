import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    custies = customers.drop_duplicates(subset=['email'])
    return custies

#QED
#Problem 2882 (Easy) - Jason Balayev (python)
