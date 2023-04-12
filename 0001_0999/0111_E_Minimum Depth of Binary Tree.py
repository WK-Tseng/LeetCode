# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0 
        queue = [root]
        while queue:
            depth += 1
            nextQueue = []
            for node in queue:
                count = 0

                if node.left:
                    nextQueue.append(node.left)
                    count += 1

                if node.right:
                    nextQueue.append(node.right)
                    count += 1
                
                if count == 0:
                    return depth

            queue = nextQueue
        
        return depth