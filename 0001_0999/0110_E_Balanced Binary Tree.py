# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def DFS(root, level):
            if root:
                left, left_balanced = DFS(root.left, level+1)
                right, right_balanced = DFS(root.right, level+1)
                return max(left, right), all([left_balanced, right_balanced, abs(left - right) <= 1])
            return level - 1, True

        _, result = DFS(root, 0)
        return result