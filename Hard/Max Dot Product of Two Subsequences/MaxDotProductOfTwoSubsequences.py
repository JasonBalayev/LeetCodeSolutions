class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        prev=[nums1[0]*nums2[0]]
        for j in range(1,n):
            prev.append(max(prev[-1],nums1[0]*nums2[j]))
        for i in range(1,m):
            curr=[max(prev[0],nums1[i]*nums2[0])]
            for j in range(1,n):
                prod=nums1[i]*nums2[j]
                curr.append(max(prev[j-1]+prod,prev[j],curr[-1],prod))
            prev=curr
        return prev[-1]

#QED
#Problem 1458 (Hard of Max Dot Product of Two Subsequences) - Jason Balayev (python)
