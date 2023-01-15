class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        bus_stop = collections.defaultdict(set)
        for idx, route in enumerate(routes):
            for _bus_stop in route:
                bus_stop[_bus_stop].add(idx)

        if source not in bus_stop or target not in bus_stop:
            return -1

        N = len(routes) + 1
        result = N
        for idx in bus_stop[source]:
            visit = set()
            queue = set([idx])
            times = 0

            while queue:
                times += 1
                if not queue.isdisjoint(bus_stop[target]):
                    result = times
                    break
                
                if times >= result:
                    break

                next_queue = set()
                for j in queue:
                    if j not in visit:
                        visit.add(j)
                        for stop in routes[j]:
                            next_queue |= bus_stop[stop]

                queue = None
                if len(next_queue) > 0:
                    queue = next_queue


        return -1 if result == N else result