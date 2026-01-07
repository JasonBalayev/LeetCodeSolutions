# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod=(10**9+7)
        queue,total=[root],[0]
        while queue:
            total[0]+=sum(node.val for node in queue)
            queue=[child for node in queue for child in(node.left,node.right)if child]
        max_prod=[0]
        def dfs(n):
            subtree_sum=n.val+(dfs(n.left)if n.left else 0)+(dfs(n.right)if n.right else 0)
            if n!=root:
                max_prod[0]=max(max_prod[0],subtree_sum*(total[0]-subtree_sum))
            return subtree_sum
        dfs(root)
        return max_prod[0]%mod

#QED
#Problem 1339 (Medium of Maximum Product of Splitted Binary Tree) - Jason Balayev (python)
