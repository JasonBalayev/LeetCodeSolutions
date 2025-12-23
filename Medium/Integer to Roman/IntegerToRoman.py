class Solution:
    def intToRoman(self, num: int) -> str:
        vals= [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res=[]
        
        for i in range(len(vals)):
            count=num//vals[i]
            if count:
                res.append(symbols[i]*count)
                num-=vals[i]*count
        return ''.join(res)

# largest standard number without bars = 3,999 (MMMCMXCIX)

#QED
#Problem 12 (Medium of Integer to Roman) - Jason Balayev (python)