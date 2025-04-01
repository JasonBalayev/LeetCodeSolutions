class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [""]

        for dig in digits:
            new_res = []
            letters = phone_mapping[dig]
            for combo in res:
                for letter in letters:
                    new_res.append(combo + letter)
            res = new_res
        return res

#QED
#Problem 17 (Medium Of Letter Combinations Of A Phone Number) - Jason Balayev (python)