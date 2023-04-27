# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def inorder(root, number):
            if root is None:
                return 
            
            number += str(root.val)
            
            inorder(root.left, number)
            
            inorder(root.right, number)
            
            if root.left is None and root.right is None:
                ans.append(int(number))
        
        inorder(root, "")
        return sum(ans)