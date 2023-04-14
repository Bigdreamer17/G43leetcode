# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = []
        def pathfinder(root, string):
            if not root:
                return
            
            string += str(root.val)
            pathfinder(root.left, string)
            pathfinder(root.right, string)
            
            if root.left is None and root.right is None:
                summ.append(int(string))
        
        pathfinder(root, "")
        return sum(summ)
        