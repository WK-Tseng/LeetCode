# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        nodeDict = collections.defaultdict(set)

        def DFS(node):
            if node:
                if node.left:
                    nodeDict[node.val].add(node.left.val)
                    nodeDict[node.left.val].add(node.val)
                    DFS(node.left)
                
                if node.right:
                    nodeDict[node.val].add(node.right.val)
                    nodeDict[node.right.val].add(node.val)
                    DFS(node.right)

        DFS(root)

        # print(nodeDict)

        queue = [target.val]
        visit = set()
        result = []
        while queue and k > 0:
            nextQueue = []
            for val in queue:
                visit.add(val)
                for nextVal in nodeDict[val]:
                    if nextVal not in visit:
                        nextQueue.append(nextVal)

            queue = nextQueue

            k -= 1

        # print(queue)

        return queue