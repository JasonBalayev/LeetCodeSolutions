
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_i_map = {}
        start = 0
        max_len = 0

        for i, char in enumerate(s):
            if char in c_i_map and c_i_map[char] >= start:
                start = c_i_map[char] + 1
            c_i_map[char] = i
            max_len = max(max_len, i -start + 1)
        return max_len

#QED
#Problem 3 (Medium Of Longest Substring Without Repeating Characters) - Jason Balayev (python)