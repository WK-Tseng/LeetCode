"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeDict = {}

        if node is None:
            return node

        queue = [node]
        visit = set()
        while queue:
            n = queue.pop(0)
            visit.add(n.val)

            next_n = None
            if n.val not in nodeDict:
                next_n = Node(n.val)
                nodeDict[next_n.val] = next_n
            else:
                next_n = nodeDict[n.val]

            if n.neighbors is not None:
                next_n.neighbors = []
                for nn in n.neighbors:
                    temp_n = None
                    if nn.val not in nodeDict:
                        temp_n = Node(nn.val)
                        nodeDict[temp_n.val] = temp_n
                    else:
                        temp_n = nodeDict[nn.val]
                    next_n.neighbors.append(temp_n)
                    
                    if temp_n.val not in visit:
                        queue.append(nn)
                
        return nodeDict[1]