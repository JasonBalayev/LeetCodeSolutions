class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0
        while x > reverse:
            reverse = (reverse * 10) + (x % 10)
            x //= 10  
        return x == reverse or x == reverse // 10
    
#QED
#Problem 9 (Palindrome Number) - Jason Balayev (python)   