# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodeStack = [[root, 0]]

        result = None

        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]

            if nowNode[1] == 0:

                nowNode[0].sumVal = nowNode[0].val

                # Left leaf
                leftNode = nowNode[0].left
                nowNode[1] = 1
                if leftNode:
                    nodeStack.append([leftNode, 0])
            elif nowNode[1] == 1:
                # Right leaf
                rightNode = nowNode[0].right
                nowNode[1] = 2
                if rightNode:
                    nodeStack.append([rightNode, 0])
            elif nowNode[1] == 2:
                if result is None:
                    result = nowNode[0].val

                tempSumVal = nowNode[0].val
                tempRootSumVal = nowNode[0].val

                if nowNode[0].left:
                    temp = nowNode[0].left.sumVal
                    tempSumVal = max(tempSumVal, nowNode[0].val + temp)
                    tempRootSumVal += temp
                
                if nowNode[0].right:
                    temp = nowNode[0].right.sumVal
                    tempSumVal = max(tempSumVal, nowNode[0].val+temp)
                    tempRootSumVal += temp

                nowNode[0].sumVal = tempSumVal
                result = max(result, tempSumVal, tempRootSumVal)

                del nodeStack[-1]

        return result