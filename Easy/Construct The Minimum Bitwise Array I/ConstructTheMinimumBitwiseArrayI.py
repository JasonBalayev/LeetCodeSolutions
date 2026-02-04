class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for target in nums:
            x=-1
            for j in range(target+1):
                if(j|(j+1))==target:
                    x=j
                    break
            ans.append(x)
        return ans

#QED
#Problem 3314 (Easy of Construct The Minimum Bitwise Array I) - Jason Balayev (python)
