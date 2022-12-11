# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        nodeList = [root]
        while nodeList:
            result.append([node.val for node in nodeList if node])
            
            nextNodeList = []
            for node in nodeList:
                if node:
                    nextNodeList += [node.left, node.right]
  
            nodeList = nextNodeList

        return result[:-1]

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     result = []
    #     if root is None:
    #         return result

    #     nodeList = [root]
    #     while nodeList:
    #         result.append([node.val for node in nodeList])

    #         nextNodeList = []
    #         for node in nodeList:
    #             if node.left:
    #                 nextNodeList.append(node.left)
    #             if node.right:
    #                 nextNodeList.append(node.right)

    #         nodeList = None
    #         if len(nextNodeList) > 0:
    #             nodeList = nextNodeList

    #     return result
