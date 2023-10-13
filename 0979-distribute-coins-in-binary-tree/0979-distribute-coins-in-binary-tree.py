# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node: 
                return 0
            Left = dfs(node.left)
            Right = dfs(node.right)
            ans += abs(Left) + abs(Right)
            return node.val + Left + Right - 1

        dfs(root)
        return ans