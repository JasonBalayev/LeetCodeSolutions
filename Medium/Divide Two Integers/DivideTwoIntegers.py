class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int = 2**31 - 1
        min_int = -2**31

        if dividend == min_int and divisor == -1:
            return max_int
        
        neg = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        divisor_multiples = []
        count_multiples = []
        curr_divisor = divisor
        curr_count = 1
        
        while curr_divisor <= dividend:
            divisor_multiples.append(curr_divisor)
            count_multiples.append(curr_count)
            curr_divisor += curr_divisor
            curr_count += curr_count
        
        for i in range(len(divisor_multiples) - 1, -1, -1):
            if dividend >= divisor_multiples[i]:
                dividend -= divisor_multiples[i]
                res += count_multiples[i]
        
        if neg:
            res = -res
        return res
    
#QED
#Problem 29 (Medium Of Divide Two Integers) - Jason Balayev (python)