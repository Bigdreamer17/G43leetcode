# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def post(root):
            nonlocal ans
            if not root:
                return 0
            
            left = post(root.left)
            right = post(root.right)
            tilt = abs(left - right)
            ans += tilt
            
            return left + right + root.val
        
        post(root)
        
        return ans