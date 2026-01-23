class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        arr=nums[:]
        ops=0
        while True:
            n=len(arr)
            if n<=1:
                break
            is_sorted=True
            for i in range(n-1):
                if arr[i]>arr[i+1]:
                    is_sorted=False
                    break
            if is_sorted:
                break
            min_sum=arr[0]+arr[1]
            min_idx=0
            for i in range(1,n-1):
                s=arr[i]+arr[i+1]
                if s<min_sum:
                    min_sum=s
                    min_idx=i
            arr[min_idx]=min_sum
            arr.pop(min_idx+1)
            ops+=1
        return ops

#QED
#Problem 3508 (Hard of Minimum Pair Removal To Sort Array II) - Jason Balayev (python)
