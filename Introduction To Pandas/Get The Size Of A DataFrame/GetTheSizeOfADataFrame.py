import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]

#QED
#Problem 2878 (Easy) - Jason Balayev (python)
