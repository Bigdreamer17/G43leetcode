# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        _sum = 0
        
        def dfs(root):
            nonlocal _sum
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        _sum += root.left.left.val
                    if root.left.right:
                        _sum += root.left.right.val
                if root.right:
                    if root.right.left:
                        _sum += root.right.left.val
                    if root.right.right:
                        _sum += root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return _sum