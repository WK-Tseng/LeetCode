# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        numSet = set()

        def DFS(node):
            if node:
                numSet.add(node.val)
                DFS(node.left)
                DFS(node.right)
        
        DFS(root)

        for n in numSet:
            if k-n in numSet and n != k-n:
                return True
        
        return False