# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # AC, fast
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkSymmetric(node_1, node_2):
            val_1 = node_1.val if node_1 else None
            val_2 = node_2.val if node_2 else None

            if val_1 is None and val_2 is None:
                return True
            elif val_1 != val_2:
                return False
            
            return checkSymmetric(node_1.left, node_2.right) and checkSymmetric(node_1.right, node_2.left)
        
        return checkSymmetric(root.left, root.right)

    # AC, slow
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    #     layer = [root]
    #     while layer:
    #         nextLayer = []
    #         for node in layer:
    #             if node:
    #                 nextLayer.extend([node.left, node.right])
    #             else:
    #                 nextLayer.extend([None, None])

    #         for i in range(len(nextLayer)//2):
    #             val_1 = None if nextLayer[i] is None else nextLayer[i].val
    #             val_2 = None if nextLayer[-(i+1)] is None else nextLayer[-(i+1)].val
                
    #             if val_1 != val_2:
    #                 return False

    #         layer = None
    #         if any(node is not None for node in nextLayer):
    #             layer = nextLayer
            
    #     return True
            
