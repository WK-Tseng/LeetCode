class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visit = {i: False for i in range(n)}

        for _, to in edges:
            visit[to] = True
            
        return [key for key, val in visit.items() if not val]