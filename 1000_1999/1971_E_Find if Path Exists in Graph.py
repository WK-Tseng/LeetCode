class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        visit = set()
        point = [source]

        while point:
            # print('-----------------------')
            # print(edges, visit, point)
            newPoint = []
            removeEdges = []
            for edge in edges:
                p1, p2 = edge
                if p1 in point or p2 in point:
                    if p1 in point and p2 not in visit:
                        newPoint.append(p2)
                    if p2 in point and p1 not in visit:
                        newPoint.append(p1)
                    visit.add(p1)
                    visit.add(p2)
                    removeEdges.append(edge)
            # print(removeEdges)
            for edge in removeEdges:
                edges.remove(edge)

            point = None
            if len(newPoint) > 0:
                point = newPoint
            # print(edges, visit)
            if destination in visit:
                return True
        
        return False