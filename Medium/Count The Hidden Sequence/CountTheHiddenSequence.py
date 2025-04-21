class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr=0
        min_val=0
        max_val=0
        for diff in differences:
            curr+=diff
            min_val=min(min_val,curr)
            max_val=max(max_val,curr)
        
        start_min=lower-min_val
        start_max=upper-max_val

        if start_min<=start_max:
            return start_max-start_min+1
        else:
            return 0
        
#QED
#Problem 2145 (Medium of Count The Hidden Sequence) - Jason Balayev (cpp)