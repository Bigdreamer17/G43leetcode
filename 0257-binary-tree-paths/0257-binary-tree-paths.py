# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def backtrack(lis, root):
            if root.left is None and root.right is None:
                ans.append(lis[:])
                
            if root.right:
                lis.append(root.right.val)
                backtrack(lis, root.right)
                lis.pop()
            if root.left:
                lis.append(root.left.val)
                backtrack(lis, root.left)
                lis.pop()
        backtrack([root.val], root)
        for indx, lisst in enumerate(ans):
            ans[indx] = "->".join(list(map(str,lisst)))
        
        return ans
                
                
            