class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        roads_dict = collections.defaultdict(list)
        for a, b, d in roads:
            roads_dict[a].append((b, d))
            roads_dict[b].append((a, d))
        
        min_d = roads_dict[1][0][1]
        queue = set([1])
        visit = set()
        while queue:
            # visit |= queue
            next_queue = set()
            for p in queue:
                for b, d in roads_dict[p]:
                    if (p, b) not in visit:
                        min_d = min(min_d, d)
                        next_queue.add(b)
                        visit.add((p, b))
                        visit.add((b, p))
            queue = next_queue

        # print(visit)
        return min_d