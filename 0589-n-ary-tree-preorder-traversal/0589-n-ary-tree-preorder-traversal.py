"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ans  = []
        
        def pre(root, ans):
            if root == None:
                return ans
            
            ans.append(root.val)
            for child in root.children:
                pre(child,ans)
                
            
            return ans
        return pre(root,ans)