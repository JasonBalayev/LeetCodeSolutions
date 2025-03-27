class Solution:
    def isValid(self, s: str) -> bool:

        dictionary = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets:
                if not dictionary or dictionary.pop() != brackets[char]:
                    return False
            else: 
                dictionary.append(char)
        return len(dictionary) == 0      
    
#QED
#Problem 20 (Valid Parentheses) - Jason Balayev (python3)