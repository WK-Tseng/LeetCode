# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def DFS(node,  valMin, valMax):
            if not node:
                return valMax - valMin
            left = DFS(node.left, valMin, node.val)
            right = DFS(node.right, node.val, valMax)
            return min(left,  right)

        return DFS(root, float('-inf'), float('inf'))