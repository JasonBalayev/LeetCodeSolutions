# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q,s=[root],[]
        while q:
            s.append(sum(n.val for n in q))
            q=[c for n in q for c in(n.left,n.right)if c]
        return s.index(max(s))+1

#QED
#Problem 1161 (Medium of Maximum Level Sum Of A Binary Tree) - Jason Balayev (python)
