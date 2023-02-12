class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        connect_non = collections.defaultdict(set)
        for a, b in roads:
            connect_non[a].add(b)
            connect_non[b].add(a)
            
        visit = set()
        def DFS(node, people):
            visit.add(node)
            cost = 0
            for np in connect_non[node]:
                if np not in visit:
                    p, c = DFS(np, 1)
                    people += p
                    cost += c

            cost += math.ceil(people/seats) if node else 0
            return people, cost

        people, cost = DFS(0, 0)
        return cost