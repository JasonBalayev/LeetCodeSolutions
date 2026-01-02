# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def travel(node,dir,len):
            if not node:
                return len-1
            if dir==0:
                return max(travel(node.left,1,len+1),travel(node.right,0,1))
            else:
                return max(travel(node.right,0,len+1),travel(node.left,1,1))
        return max(travel(root.left,1,1),travel(root.right,0,1))

#QED
#Problem 1372 (Medium of Longest ZigZag Path In A Binary Tree) - Jason Balayev (python)