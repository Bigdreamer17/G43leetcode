# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, TotalSum) -> bool:
            if not root:
                return 
            elif not root.left and not root.right:
                return TotalSum + root.val == targetSum
            else:
                return dfs(root.left, TotalSum + root.val) or dfs(root.right, TotalSum + root.val)
            
        if root:
            return dfs(root, 0)