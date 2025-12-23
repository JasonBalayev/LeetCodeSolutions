class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        res=0
        max_end=0
        j=0
        events.sort(key=lambda x:x[0])
        end=sorted(events,key=lambda x:x[1])
        for s,e,v in events:
            while j<len(end) and end[j][1]<s:
                max_end=max(max_end,end[j][2])
                j+=1
            res=max(res,max_end+v)
        return res

#QED
#Problem 2054 (Medium of Two Best Non-Overlapping Events) - Jason Balayev (python)