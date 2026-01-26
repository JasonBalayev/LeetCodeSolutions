class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        min_diff=arr[1]-arr[0]
        res.append([arr[0],arr[1]])
        for i in range(1,len(arr)-1):
            diff=arr[i+1]-arr[i]
            if diff<min_diff:
                min_diff=diff
                res=[[arr[i],arr[i+1]]]
            elif diff==min_diff:
                res.append([arr[i],arr[i+1]])
        return res

#QED
#Problem 1200 (Easy of Minimum Absolute Difference) - Jason Balayev (python)
