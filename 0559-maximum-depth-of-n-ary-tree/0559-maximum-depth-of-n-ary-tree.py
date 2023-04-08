"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        maxdepth = 0
        
        
        for child in root.children:
            maxdepth = max(maxdepth, self.maxDepth(child))
        
        
        return maxdepth + 1