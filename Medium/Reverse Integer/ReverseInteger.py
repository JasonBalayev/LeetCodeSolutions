class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x:
            result = result * 10 + x % 10
            x //= 10
            
        result *= sign
        return result if -2**31 <= result <= 2**31 - 1 else 0

#QED
#Problem 7 (Reverse Integer) - Jason Balayev (python3)