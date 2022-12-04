class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = []
        self.path = 1

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        if parent is None or len(parent) == 0:
            return 0

        nodeList = []
        for i in range(len(parent)):
            tempNode = TreeNode(s[i])
            nodeList.append(tempNode)

        for i in range(1, len(parent)):
            parentIdx = parent[i]
            nodeList[parentIdx].child.append(nodeList[i])

        root = nodeList[0]
        nodeStack = [[root, 0]]
        result = 0
        
        while len(nodeStack) != 0:
            nowNode = nodeStack[-1]
            
            if nowNode[1] < len(nowNode[0].child):
                nextNode = nowNode[0].child[nowNode[1]]
                nowNode[1] += 1
                nodeStack.append([nextNode, 0])
            else:
                thisVal = nowNode[0].val
                thisPath = 1
                pathList = []

                for tempNode in nowNode[0].child:
                    if tempNode.val != thisVal:
                        thisPath = max(thisPath, tempNode.path + 1)
                        
                        if len(pathList) < 2:
                            pathList.append(tempNode.path)
                        else:
                            pathList.append(tempNode.path)
                            pathList.sort()
                            del pathList[0]

                rootPath = 1 + sum(pathList)
                nowNode[0].path = thisPath
                
                result = max(result, thisPath, rootPath)
                del nodeStack[-1]

        return result
        