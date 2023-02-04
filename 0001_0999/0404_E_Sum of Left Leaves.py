# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        result = [0]

        def DFS(node, is_left):
            if node:
                if is_left and node.left is None and node.right is None:
                    result[0] += node.val
                else:
                    DFS(node.left, True)
                    DFS(node.right, False)

        DFS(root, False)

        return result[0]