class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        n=len(nums1)
        pos2={}
        for i in range(n):
            pos2[nums2[i]] = i
        
        mapped = [pos2[nums1[i]] for i in range(n)]
        bit = [0]*(n+1)

        def update(idx,val):
            idx +=1
            while idx<=n:
                bit[idx] += val
                idx += idx&-idx
            
        def query(idx):
            idx+=1
            res=0
            while idx>0:
                res+= bit[idx]
                idx -= idx&-idx
            return res
        res = 0

        for j in range(n):
            smaller_left = query(mapped[j]-1)
            larger_right = n-mapped[j] - 1-(j-smaller_left)
            res += smaller_left*larger_right
            update(mapped[j],1)
        return res
    
#QED
#Problem 2179 (Hard of Count Good Triplets In An Array) - Jason Balayev (python)

