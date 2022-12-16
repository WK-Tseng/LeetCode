# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def FindDepthDFS(node, depth):
            if node:
                return max(FindDepthDFS(node.left, depth + 1), FindDepthDFS(node.right, depth + 1))
            return depth - 1

        return FindDepthDFS(root, 1)
