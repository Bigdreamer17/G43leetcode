# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        Root = TreeNode(preorder[0])
        decreasing = [Root]
        
        for i in range(1, len(preorder)):
            newNode = TreeNode(preorder[i])
            if not decreasing or decreasing[-1].val > newNode.val:
                decreasing[-1].left = newNode
                decreasing.append(newNode)
            
            else:
                while decreasing and decreasing[-1].val < newNode.val:
                    removed = decreasing.pop()
                removed.right = newNode
                decreasing.append(newNode)  
        return Root