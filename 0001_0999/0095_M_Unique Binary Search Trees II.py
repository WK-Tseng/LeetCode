# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def trees(s, e):
            return [TreeNode(root, left, right) for root in range(s, e+1) for left in trees(s, root-1) for right in trees(root+1, e)] or [None]

        return trees(1, n)