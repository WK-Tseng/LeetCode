# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        result = (root.val, 0)
        queue = []
        queue.append((root, 0))

        while queue:
            node, layer = queue.pop(0)
            if layer > result[1]:
                result = (node.val, layer)
            
            if node.left:
                queue.append((node.left, layer+1))
            
            if node.right:
                queue.append((node.right, layer+1))

        return result[0]