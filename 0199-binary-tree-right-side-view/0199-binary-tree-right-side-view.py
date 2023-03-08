# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root is None:
            return 
        
        Q = deque()
        Q.append(root)
        
        while Q:
            cur_size = len(Q)
            cur_list = []
            
            while cur_size > 0:
                cur_node = Q.popleft()
                cur_list.append(cur_node.val)
                cur_size -= 1
                
                if cur_node.left is not None:
                    Q.append(cur_node.left)
                if cur_node.right is not None:
                    Q.append(cur_node.right)
            
            ans.append(cur_list[-1])
        return ans