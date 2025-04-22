class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        modulo=10**9+7
        comb = [[0]*(min(n,15)+1) for x in range(n+1)]

        for i in range(n+1):
            comb[i][0]=1
            for j in range(1,min(i,min(n,15))+1):
                comb[i][j]=(comb[i-1][j-1]+comb[i-1][j]) % modulo
        
        dp={}
        
        def count(length,last_val):
            if length==1:
                return 1
            if(length,last_val) in dp:
                return dp[(length,last_val)]
            total=0
            i=1
            while i*i<=last_val:
                if last_val%i==0:
                    if i<last_val:
                        total = (total+count(length-1,i)) % modulo
                    other_divisor=last_val//i
                    if other_divisor!= i and other_divisor<last_val:
                        total = (total+count(length-1,other_divisor)) % modulo
                i+=1
            dp[(length,last_val)]=total
            return total
        res=0

        for val in range(1,maxValue+1):
            for length in range(1,min(n,15)+1):
                ways=count(length,val)
                res=(res+ways*comb[n-1][length-1]) % modulo
        return res  
    
#QED
#Problem 2338 (Hard of Count The Number Of Ideal Arrays) - Jason Balayev (python)  
