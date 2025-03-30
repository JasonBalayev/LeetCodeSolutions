class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s:
            return ""

        res = [s[0]]
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                count = 1
            if count < 3:
                res.append(s[i])
        return ''.join(res)
    
#QED
#Problem 1957 (Easy Of Delete Characters to Make Fancy String) - Jason Balayev (python)