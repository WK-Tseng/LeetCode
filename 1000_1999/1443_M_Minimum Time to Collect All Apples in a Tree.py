class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        edge_dict = collections.defaultdict(set)
        for p1, p2 in edges:
            edge_dict[p1].add(p2)
            edge_dict[p2].add(p1)

        # print(edge_dict)

        visit = set()
        queue = [0]
        while queue:
            next_queue = []
            for start in queue:
                visit.add(start)
                remove_p = set()
                for p in edge_dict[start]:
                    if p in visit:
                        remove_p.add(p)
                    else:
                        next_queue.append(p)
                edge_dict[start] -= remove_p
                
            queue = None
            if len(next_queue) > 0:
                queue = next_queue

        # print(visit)
        # print(edge_dict)

        def DFS(start):
            # print(start)
            cost = 0
            for p in edge_dict[start]:
                cost += DFS(p)
            
            
            if cost == 0 and hasApple[start]:
                cost =  1
            elif cost != 0:
                cost += 1
            else:
                cost = 0
            
            return cost

        result = DFS(0)
        result = max(DFS(0) - 1, 0) * 2

        return result