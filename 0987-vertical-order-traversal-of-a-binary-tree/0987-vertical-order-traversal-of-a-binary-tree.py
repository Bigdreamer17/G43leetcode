# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        freq = {}
        
        def traversal(root, row = 0, col = 0):
            if not root:
                return
            if col not in freq:
                freq[col] = []
            freq[col].append((row, root.val))
            
            traversal(root.left, row + 1, col - 1)
            traversal(root.right, row + 1, col + 1)
        traversal(root)
        ans = []
        for i in sorted(freq.keys()):
            freq[i].sort()
            for j in range(len(freq[i])):
                freq[i][j] = freq[i][j][1]
            ans.append(freq[i])
        return ans
            