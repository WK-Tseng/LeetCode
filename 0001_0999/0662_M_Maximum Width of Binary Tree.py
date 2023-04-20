# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 1

        queue = [(root, 1)]
        while queue:
            next_queue = []

            thisMin = queue[0][1]
            thisMax = queue[0][1]

            for node, i in queue:
                
                thisMin = min(thisMin, i)
                thisMax = max(thisMax, i)

                j = i << 1

                if node.left:
                    next_queue.append((node.left, j-1))
                if node.right:
                    next_queue.append((node.right, j))

            result = max(result, thisMax-thisMin+1)
            queue = next_queue

        return result