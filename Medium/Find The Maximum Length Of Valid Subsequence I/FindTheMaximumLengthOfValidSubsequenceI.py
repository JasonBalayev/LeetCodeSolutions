class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even=0
        for num in nums:
            if num%2==0:
                even+=1
        odd=len(nums)-even
        max_p=max(even,odd)
        start_even=0
        need_even=0
        for num in nums:
            if num%2==need_even:
                start_even+=1
                need_even=1-need_even
        start_odd=0
        need_odd=1
        for num in nums:
            if num%2==need_odd:
                start_odd+=1
                need_odd=1-need_odd
        max_a=max(start_even,start_odd)
        return max(max_p,max_a)
    
    #QED
    #Problem 3201 (Medium Of Find The Maximum Length Of Valid Subsequence I) - Jason Balayev (python)