# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftSum = 0
        def dfs(root, nType):
            nonlocal leftSum
            if root:
                if not root.left and not root.right and nType == "left":
                    leftSum += root.val
                dfs(root.left, "left")
                dfs(root.right, "right")

        dfs(root, "any")
        return leftSum