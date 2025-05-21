# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums={0:1}
        total_paths=0
        def dfs(node,curr_sum):
            nonlocal total_paths
            if not node:
                return
            curr_sum+=node.val
            c=curr_sum-targetSum
            if c in prefix_sums:
                total_paths+=prefix_sums[c]
            prefix_sums[curr_sum]=prefix_sums.get(curr_sum,0)+1
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            prefix_sums[curr_sum]-=1
        dfs(root,0)
        return total_paths

#QED
#Problem 437 (Medium of Path Sum III) - Jason Balayev (python)