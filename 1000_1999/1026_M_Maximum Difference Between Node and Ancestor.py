# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def DFS(root, minVal, maxVal):
            if root:
                minVal = min(root.val, minVal)
                maxVal = max(root.val, maxVal)
                absVal = abs(maxVal - minVal)
                return max(absVal, DFS(root.left, minVal, maxVal), DFS(root.right, minVal, maxVal))
            else:
                absVal = abs(maxVal - minVal)
                return absVal

        return DFS(root, root.val, root.val)