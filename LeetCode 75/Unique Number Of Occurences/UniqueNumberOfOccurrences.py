class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        return len(count.values())==len(set(count.values()))
    
#QED
#Problem 1207 (Easy of Unique Number Of Occurences) - Jason Balayev (python)