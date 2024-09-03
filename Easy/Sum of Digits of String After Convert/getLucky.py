class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num_str = ''.join(str(ord(char) - ord('a') +1) for char in s)
        result = sum(int(digit) for digit in num_str)
        for i in range(1, k):
            result = sum(int(digit) for digit in str(result))
        return result
    
#QED
#Problem 1945 (Daily Problem: Sum of Digits of String After Convert) - Jason Balayev (python)   