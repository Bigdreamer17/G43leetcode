# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both are empty
        if not p and not q:
            return True
        # Check if either is empty
        if not p or not q:
            return False
        # Check value
        if p.val != q.val:
            return False
        # traverse simultaneously 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)