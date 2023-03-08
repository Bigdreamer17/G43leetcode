# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        ans = []
        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)
        
        freq = Counter(arr)
        mode = -float('inf')
        for i in arr:
            mode = max(mode, freq[i])
        for key,value in freq.items():
            if value == mode:
                ans.append(key)
        return ans