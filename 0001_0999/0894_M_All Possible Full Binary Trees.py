# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        n -= 1

        if n == 0:
            return [TreeNode()]

        result = []
        for count in range(1, n, 2):
            for left in self.allPossibleFBT(count):
                for right in self.allPossibleFBT(n - count):
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    result.append(root)

        return result