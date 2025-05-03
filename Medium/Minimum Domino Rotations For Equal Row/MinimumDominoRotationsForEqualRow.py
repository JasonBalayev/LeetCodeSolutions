class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n=len(tops)
        poss_val=[tops[0],bottoms[0]]
        for val in poss_val:
            top_swaps=0
            bot_swaps=0
            equal=True
            for i in range(n):
                if tops[i]!=val and bottoms[i]!=val:
                    equal=False
                    break
                if tops[i]!=val:
                    top_swaps+=1
                if bottoms[i]!=val:
                    bot_swaps+=1
            if equal:
                return min(top_swaps,bot_swaps)
        return -1
    
#QED
#Problem 1007 (Medium of Minimum Domino Rotations For Equal Row) - Jason Balayev (python)