# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = 0
        
        def post(root, targetSum):
            nonlocal path
            
            if not root:
                return
            
            post(root.left, targetSum)
            post(root.right, targetSum)
            helper(root, targetSum)
        
        def helper(root, targetSum):
            nonlocal path
            if not root:
                return
            
            if root.val == targetSum:
                path += 1
                
                
            helper(root.left, targetSum - root.val)
            helper(root.right,targetSum - root.val)
            
        post(root, targetSum)
        return path
        