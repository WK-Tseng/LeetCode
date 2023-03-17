# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        path = []

        def DFS(root):
            if root:
                path.append(str(root.val))
                if not root.left and not root.right:
                    result.append('->'.join(path))
                else:
                    DFS(root.left)
                    DFS(root.right)
                path.pop(-1)

        DFS(root)

        return result