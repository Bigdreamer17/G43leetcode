# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def dfs(root):
            if root:
                dfs(root.left)
                nums.append(root.val)
                dfs(root.right)

        dfs(root)
        
        root = tree = TreeNode(0)
        for i in range(len(nums)):
            tree.right = TreeNode(nums[i])
            tree = tree.right

        
        return root.right
        