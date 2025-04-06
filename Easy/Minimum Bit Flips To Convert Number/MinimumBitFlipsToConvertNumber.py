class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start^goal
        count = 0
        while res:
            count += res & 1
            res >>= 1
        return count
        
#QED
#Problem 2220 (Easy Of Minimum Bit Flips To Convert Number) - Jason Balayev (python)