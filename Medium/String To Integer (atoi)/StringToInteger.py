class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        sign = 1
        index = 0

        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1

        num = 0

        for i in range(index, len(s)):
            if not s[i].isdigit():
                break
            num = num * 10 + int(s[i])

        num *= sign
        int_min = -2**31 
        int_max = 2**31 - 1

        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        return num

#QED
#Problem 8 (Medium Of String to Integer (atoi)) - Jason Balayev (python)