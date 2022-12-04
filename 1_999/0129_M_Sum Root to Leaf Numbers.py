# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getNumber(self, nodeStack):
        strNumber = ''
        for node in nodeStack:
            strNumber += str(node[0].val)

        return int(strNumber)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodeStack = [[root, 0]]

        result = 0

        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]

            if nowNode[1] == 0:
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
                    if nowNode[0].left is None:
                        result += self.getNumber(nodeStack)

                    del nodeStack[-1]
            elif nowNode[1] == 2:
                del nodeStack[-1]

        return result