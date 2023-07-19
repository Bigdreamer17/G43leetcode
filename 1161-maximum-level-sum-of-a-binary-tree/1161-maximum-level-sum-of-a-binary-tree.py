# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum , ans , level = float('-inf'), 0 , 0
        q = collections.deque()
        q.append(root)
        
        while q:
            level += 1
            cur_sum = 0
            
            for i in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < cur_sum:
                max_sum, ans = cur_sum, level
        return ans