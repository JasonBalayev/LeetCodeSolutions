# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs=lambda n:(0,None)if not n else(
            lambda l,r:(l[0]+1,n)if l[0]==r[0]
            else((l[0]+1,l[1])if l[0]>r[0]else(r[0]+1,r[1]))
        )(dfs(n.left),dfs(n.right))
        return dfs(root)[1]
#QED
#Problem 865 (Medium of Smallest Subtree With All The Deepest Nodes) - Jason Balayev (python)
