# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        nodeStack = [[root, 0]]
        result = True

        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]

            if nowNode[1] == 0:

                nowNode[0].minVal = nowNode[0].val
                nowNode[0].maxVal = nowNode[0].val

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

                if nowNode[0].left:
                    if nowNode[0].left.maxVal < nowNode[0].val:
                        nowNode[0].minVal = nowNode[0].left.minVal
                    else:
                        result = False
                        break

                if nowNode[0].right:
                    if nowNode[0].right.minVal > nowNode[0].val:
                        nowNode[0].maxVal = nowNode[0].right.maxVal
                    else:
                        result = False
                        break
                
                del nodeStack[-1]
        
        return result
