# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            leftdepth = self.maxDepth(root.left)
            rightdepth = self.maxDepth(root.right)
            
            if leftdepth > rightdepth:
                return leftdepth + 1
            else:
                return rightdepth + 1