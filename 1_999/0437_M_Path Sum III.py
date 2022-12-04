# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkPath(self, nodeStack, targetSum):
        total = 0
        count = 0
        for i in range(len(nodeStack)-1, -1, -1):
            total += nodeStack[i][0].val
            if total == targetSum:
                count += 1

        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        nodeStack = [[root, 0]]

        result = 0

        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]

            if nowNode[1] == 0:

                result += self.checkPath(nodeStack, targetSum)

                # Left leaf
                leftNode = nowNode[0].left
                if leftNode:
                    nowNode[1] = 1
                    nodeStack.append([leftNode, 0])
                else:
                    nowNode[1] = 1
            elif nowNode[1] == 1:
                # Right leaf
                rightNode = nowNode[0].right
                if rightNode:
                    nowNode[1] = 2
                    nodeStack.append([rightNode, 0])
                else:
                    del nodeStack[-1]
            elif nowNode[1] == 2:
                del nodeStack[-1]

        return result