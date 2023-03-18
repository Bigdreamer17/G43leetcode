# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return
        ans = []
        
        def backtrack(lis, root, targetSum):
             # Goal
            if not root.left and not root.right and root.val == targetSum:
                ans.append(lis[:] + [root.val])
                return
            # Choices
            if root.right:
                backtrack(lis + [root.val], root.right, targetSum - root.val)
            
            if root.left:
                backtrack(lis + [root.val], root.left, targetSum - root.val)
        
        backtrack([],root, targetSum)
        return ans