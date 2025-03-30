class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        
        chars = {}

        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = [i,i,False]
            else:
                chars[c][1] = i

        res = []
        start = 0
        active = set()

        for i, c in enumerate(s):
            info = chars[c]
            if not info[2]:
                info[2] = True
                active.add(c)
            if i == info[1]:
                active.remove(c)
            if not active:
                size = i - start + 1
                res.append(size)
                start = i + 1
        return res

#QED
#Problem 763 (Medium Of Partition Labels) - Jason Balayev (python)