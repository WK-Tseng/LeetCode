# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        queue = [root]
        while queue:
            nextQueue = []
            count = len(queue)
            total = 0
            for node in queue:
                total += node.val
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)

            queue = nextQueue

            result.append(total/count)

        return result