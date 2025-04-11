import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=employees['salary']*2
    return employees

#QED
#Problem 2881 (Easy) - Jason Balayev (python)

