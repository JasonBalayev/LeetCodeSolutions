class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops=0
        arr=nums[:]
        while len(arr)>1 and any(arr[i]>arr[i+1]for i in range(len(arr)-1)):
            min_sum=arr[0]+arr[1]
            min_idx=0
            for i in range(len(arr)-1):
                if arr[i]+arr[i+1]<min_sum:
                    min_sum=arr[i]+arr[i+1]
                    min_idx=i
            arr[min_idx:min_idx+2]=[min_sum]
            ops+=1
        return ops
        

#QED
#Problem 3507 (Easy of Minimum Pair Removal To Sort Array I) - Jason Balayev (python)