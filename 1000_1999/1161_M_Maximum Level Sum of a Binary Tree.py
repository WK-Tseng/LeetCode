# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [(1, root)]
        sumDict = collections.defaultdict(int)

        while queue:
            level, node = queue.pop(0)

            if node:
                sumDict[level] += node.val
            
                nextLevel = level + 1
                queue.append((nextLevel, node.left))
                queue.append((nextLevel, node.right))

        maxLevel = 1
        for level in sumDict:
            if sumDict[level] > sumDict[maxLevel]:
                maxLevel = level

        return maxLevel
