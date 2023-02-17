# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        data = []

        def DFS(node):
            if node:
                data.append(node.val)
                DFS(node.left)
                DFS(node.right)

        DFS(root)
        data.sort()
        return min(data[i] - data[i-1] for i in range(1, len(data)))