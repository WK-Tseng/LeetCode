class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        visit = set()
        target = (1 << n) - 1
        queue = set((i, 1 << i) for i in range(n))
        count = 0

        while queue:
            
            visit |= queue
            next_queue = set()

            for p, s in queue:
                if s == target:
                    return count

                for next_p in graph[p]:
                    temp_tuple = (next_p, s | (1 << next_p))
                    if temp_tuple not in visit:
                        next_queue.add(temp_tuple)

            queue = next_queue
            count += 1

