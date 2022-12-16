# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        layer = [root]
        while layer:
            nextLayer = []
            for node in layer:
                if node:
                    nextLayer.append(node.left)
                    nextLayer.append(node.right)
                else:
                    nextLayer.append(None)
                    nextLayer.append(None)

            for i in range(len(nextLayer)//2):
                val_1 = None if nextLayer[i] is None else nextLayer[i].val
                val_2 = None if nextLayer[-(i+1)] is None else nextLayer[-(i+1)].val
                
                if not val_1 == val_2:
                    return False

            layer = None
            if any(node is not None for node in nextLayer):
                layer = nextLayer
            
        return True
            
