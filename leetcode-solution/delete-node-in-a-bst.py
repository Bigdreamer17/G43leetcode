# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, node):
        curr = node
        
        while curr.left != None:
            curr = curr.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None and root.right == None:
                return None
            if root.left == None:
                temp = root.right
                root = None
                return temp
            if root.right == None:
                temp = root.left
                root = None
                return temp
            temp = self.minNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root