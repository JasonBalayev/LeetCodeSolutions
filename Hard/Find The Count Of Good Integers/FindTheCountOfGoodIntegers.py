class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        mod = 10**9 +7
        mid_len = (n + 1) //2
        first = 10**(mid_len-1)
        last = 10**mid_len
        hash_set = set()
        
        def nCr(n,k):
            if k<0 or k>n:
                return 0
            if k==0 or k==n:
                return 1

            result = 1
            for i in range(1,k + 1):
                result = (result*(n-(i-1))) //i
            return result
        
        for prefix in range(first, last):
            prefix_str = str(prefix)
            palindrome = prefix_str+prefix_str[::-1] if n%2==0 else prefix_str+prefix_str[:-1][::-1]
            
            if int(palindrome) % k==0:
                counts = [0]*10
                for digit in palindrome:
                    counts[int(digit)]+=1
                
                code=0
                for c in counts:
                    code = code * 11+c
                hash_set.add(code)

        answer=0
        for code in hash_set:
            counts = [0] * 10
            
            temp_code = code
            for i in range(9,-1,-1):
                counts[i] = temp_code %11
                temp_code //=11
            
            slots = n
            arranged = 1
            for digit in range(10):
                digit_count = counts[digit]
                if digit_count>slots:
                    arranged=0
                    break
                if digit==0:
                    if digit_count>0:
                        arranged = (arranged*nCr(slots -1, digit_count))%mod
                else:
                    arranged = (arranged *nCr(slots, digit_count)) % mod
                slots -= digit_count
            answer = (answer+arranged) % mod
        return answer
    

#QED
#Problem 3272 (Hard of Find The Count Of Good Integers) - Jason Balayev (python)
