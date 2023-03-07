# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val > root.val:
            self.insertIntoBST(root.right, val)
        if val < root.val:
            self.insertIntoBST(root.left, val)
        if val > root.val and root.right == None:
            root.right = TreeNode(val)
        if val < root.val and root.left == None:
            root.left = TreeNode(val)
        
        return root