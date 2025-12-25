from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total=0
        for i in range(k):
            total+=max(0,happiness[i]-i)
        return total

#QED
#Problem 3075 (Medium of Maximize Happiness of Selected Children) - Jason Balayev (python)