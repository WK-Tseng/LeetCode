# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        nowSum = root.val
        nodeStack = [[root, 0]]

        result = False

        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]

            if nowNode[1] == 0:
                # Left leaf
                leftNode = nowNode[0].left
                if leftNode:
                    nowSum += leftNode.val
                    nowNode[1] = 1
                    nodeStack.append([leftNode, 0])
                else:
                    nowNode[1] = 1
            elif nowNode[1] == 1:
                # Right leaf
                rightNode = nowNode[0].right
                if rightNode:
                    nowSum += rightNode.val
                    nowNode[1] = 2
                    nodeStack.append([rightNode, 0])
                else:
                    if nowNode[0].left is None and nowSum == targetSum:
                        result = True
                        break
                    else:
                        nowSum -= nowNode[0].val
                        del nodeStack[-1]
            elif nowNode[1] == 2:
                nowSum -= nowNode[0].val
                del nodeStack[-1]

        return result
                
            