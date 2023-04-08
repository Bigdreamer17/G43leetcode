"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def post(root,ans):
            if root == None:
                return ans
            
            for child in root.children:
                post(child, ans)
            ans.append(root.val)
            
            
            return ans
        return post(root, ans)