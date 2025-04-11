import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.assign(grade=students['grade'].astype(int))

#QED
#Problem 2886 (Easy) - Jason Balayev (python)


