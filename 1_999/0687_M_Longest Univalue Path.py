# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodeStack = [[root, 0]]

        result = 0

        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]

            if nowNode[1] == 0:
                
                nowNode[0].path = 0

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

                thisVal = nowNode[0].val
                
                tempPath = 0

                tempRootPath = 0
                tempRootPathFlag = 0

                if nowNode[0].left and nowNode[0].left.val == thisVal:
                    temp = nowNode[0].left.path + 1
                    tempPath = max(tempPath, temp)
                    tempRootPathFlag += 1

                if nowNode[0].right and nowNode[0].right.val == thisVal:
                    temp = nowNode[0].right.path + 1
                    tempPath = max(tempPath, temp)
                    tempRootPathFlag += 1

                if tempRootPathFlag == 2:
                    tempRootPath = nowNode[0].left.path + nowNode[0].right.path + 2

                nowNode[0].path = tempPath
                result = max(result, tempPath, tempRootPath)

                del nodeStack[-1]
        
        return result