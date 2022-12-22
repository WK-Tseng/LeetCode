class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        connectDict = {i: [] for i in range(n)}
        for a, b in edges:
            connectDict[a].append(b)
            connectDict[b].append(a)

        # print(connectDict)

        treeSize = [0] * n
        childDist = [0] * n
        ans = [0] * n

        def DFS1(node, parent):
            for child in connectDict[node]:
                if child != parent:
                    DFS1(child, node)
                    treeSize[node] += treeSize[child]
                    childDist[node] += childDist[child] + treeSize[child]
            treeSize[node] += 1

        def DFS2(node, parent, dpVal):
            ans[node] = childDist[node] + dpVal + (n - treeSize[node])

            for child in connectDict[node]:
                if child != parent:
                    DFS2(child, node, ans[node] - childDist[child] - treeSize[child]) 

        DFS1(0, 0)
        DFS2(0, 0, 0)

        return ans