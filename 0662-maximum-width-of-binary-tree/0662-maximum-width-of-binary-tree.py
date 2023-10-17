# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def max_width(root):
            
            if not root:
                return 0

            max_width = 0
            queue = deque([(root, 0)])

            while queue:
                size = len(queue)
                left = float('inf')
                right = float('-inf')
                for _ in range(size):
                    node, pos = queue.popleft()
                    left = min(left, pos)
                    right = max(right, pos)
                    if node.left:
                        queue.append((node.left, 2 * pos))
                    if node.right:
                        queue.append((node.right, 2 * pos + 1))
                max_width = max(max_width, right - left + 1)

            return max_width
        
        return max_width(root)