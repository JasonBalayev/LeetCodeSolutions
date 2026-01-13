class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        target=sum(li*li for _,_,li in squares)/2.0
        left,right=min(yi for _,yi,_ in squares),max(yi+li for _,yi,li in squares)
        while right-left>1e-6:
            mid=(left+right)/2.0
            area=sum(li*li if mid>=yi+li else li*max(0,mid-yi)for _,yi,li in squares)
            if area>=target:
                right=mid
            else:
                left=mid
        return right

#QED
#Problem 3453 (Medium of Separate Squares I) - Jason Balayev (python)
