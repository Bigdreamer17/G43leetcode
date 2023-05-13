# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(node):
            if node is None:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            return max(left,right) + 1
        
        def helper(root):
            if root is None:
                return True
            left_height = maxDepth(root.left)
            right_height = maxDepth(root.right)
            
            if abs(left_height - right_height) > 1:
                return False
            left = helper(root.left)
            right = helper(root.right)
            
            if not left or not right:
                return False
            return True
        return helper(root)
        