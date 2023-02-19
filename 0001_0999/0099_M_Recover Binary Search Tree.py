# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.preNode = None
        self.error1, self.error2 = None, None

        def DFS(node):
            if node:
                DFS(node.left)
                if self.preNode and self.preNode.val > node.val:
                    if not self.error1:
                        self.error1 = self.preNode
                    self.error2 = node
                self.preNode = node
                DFS(node.right)

        DFS(root)
        self.error1.val, self.error2.val = self.error2.val, self.error1.val