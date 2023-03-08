# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        values = []
        def isSameTree(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
            else:
                return False
        p =  root.left
        q = root.right
        return isSameTree(p, q)