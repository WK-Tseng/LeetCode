# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def DFS(root, k):
            target_val = None

            if root:
                k, target_val = DFS(root.left, k)

                k -= 1
                if k == 0:
                    target_val = root.val

                if target_val is not None:
                    return k, target_val
                
                k, target_val = DFS(root.right, k)

            return k, target_val
                
        _, target_val = DFS(root, k)

        return target_val