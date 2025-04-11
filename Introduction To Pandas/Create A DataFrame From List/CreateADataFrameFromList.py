import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

#QED
#Problem 2877 (Easy) - Jason Balayev (python)
