import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    n = students[students['student_id']==101]
    return n[['name','age']]

#QED
#Problem 2880 (Easy) - Jason Balayev (python)
