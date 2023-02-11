class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connect_non = collections.defaultdict(set)
        connect_set = set()

        for a, b in connections:
            connect_non[a].add(b)
            connect_non[b].add(a)
            connect_set.add((a, b))

        count = 0
        visit = set()
        queue = set([(-1, 0)])
        while queue:
            next_queue = set()

            for _, p in queue:
                visit.add(p)

            for last, p in queue:
                for next_p in connect_non[p]:
                    if next_p not in visit:
                        temp_connect = (p, next_p)
                        next_queue.add(temp_connect)
                        if temp_connect in connect_set:
                            count += 1
            
            queue = next_queue

        return count