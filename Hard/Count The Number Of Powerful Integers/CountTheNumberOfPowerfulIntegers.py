class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        if any(int(digit) > limit for digit in suffix):
            return 0
        
        s_len = len(suffix)
        s_num = int(suffix)
        
        def count_up(num):
            dp_table = {}
            n = len(num)

            def dp(pos, tight):
                if pos==n:
                    return 1
                key = (pos, tight)
                if key in dp_table:
                    return dp_table[key]
                res = 0
                if pos >= n-s_len:
                    digit = int(suffix[pos - (n-s_len)])
                    if tight and digit > int(num[pos]):
                        dp_table[key] = 0
                        return 0
                    if digit <= limit:
                        res += dp(pos +1, tight and digit == int(num[pos]))
                else:
                    upper = int(num[pos]) if tight else limit
                    for d in range(0,upper+1):
                        if d<=limit:
                            res += dp(pos+1, tight and d == int(num[pos]))
                dp_table[key] = res
                return res
            return dp(0,True)

        if finish < s_num:
            return 0
        count_finish = count_up(str(finish))
        if start-1 < s_num:
            count_start_minus_one = 0
        else:
            count_start_minus_one = count_up(str(start-1))
        return count_finish-count_start_minus_one
    
#QED
#Problem 2999 (Hard of Count the Number of Powerful Integers) - Jason Balayev (python)
