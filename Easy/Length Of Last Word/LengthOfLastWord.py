class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.strip().split()

        if word:
            return len(word[-1])
        return 0
    
#QED
#Problem 58 (Easy Of Length Of Last Word) - Jason Balayev (python)
        