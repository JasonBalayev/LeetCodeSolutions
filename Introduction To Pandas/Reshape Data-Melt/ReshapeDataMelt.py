import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=['product'], var_name='quarter', value_name='sales')

#QED
#Problem 2890 (Easy) - Jason Balayev (python)



