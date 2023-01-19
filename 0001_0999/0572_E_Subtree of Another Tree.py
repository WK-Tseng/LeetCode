# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def DFS(node):
            if node:
                return f',{node.val},{DFS(node.left)},{DFS(node.right)}'
            else:
                return 'X'

        sRoot = DFS(root)
        sSubRoot = DFS(subRoot)

        # print(sRoot)
        # print(sSubRoot)

        return sRoot.find(sSubRoot) != -1