class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<4:
            return False
        for p in range(1,n-2):
            valid_p=True
            for i in range(p):
                if nums[i]>=nums[i+1]:
                    valid_p=False
                    break
            if not valid_p:
                continue
            for q in range(p+1,n-1):
                valid_q=True
                for i in range(p,q):
                    if nums[i]<=nums[i+1]:
                        valid_q=False
                        break
                if not valid_q:
                    continue
                valid_r=True
                for i in range(q,n-1):
                    if nums[i]>=nums[i+1]:
                        valid_r=False
                        break
                if valid_r:
                    return True
        return False

#QED
#Problem 3637 (Easy of Trionic Array I) - Jason Balayev (python)
