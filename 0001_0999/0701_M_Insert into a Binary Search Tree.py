# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def DFS(root):
            if root:
                if root.val == val:
                    # root
                    pass
                elif root.val < val:
                    node = DFS(root.right)
                    if node is not None:
                        root.right = node
                else:
                    node = DFS(root.left)
                    if node is not None:
                        root.left = node
            else:
                return TreeNode(val)

        node = DFS(root)
        return root or node