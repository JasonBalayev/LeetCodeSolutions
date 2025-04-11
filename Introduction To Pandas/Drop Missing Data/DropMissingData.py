import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    return students

#QED
#Problem 2883 (Easy) - Jason Balayev (python)


