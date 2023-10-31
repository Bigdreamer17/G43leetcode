# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        def dfs(root):
            if root:
                root.left, root.right = dfs(root.left), dfs(root.right)
                if root.val not in to_delete:
                    return root
                result.append(root.left)
                result.append(root.right)
        result.append(dfs(root))
        return ([a for a in result if a])
