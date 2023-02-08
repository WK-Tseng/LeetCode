class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)

        island = []
        one_visit = set()

        for y in range(n):
            for x in range(n):
                point = (y, x)
                if grid[y][x] == 1 and point not in one_visit:
                    visit = set()
                    queue = set()
                    queue.add(point)
                    while queue:
                        next_queue = set()
                        visit |= queue
                        for p in queue:
                            for add in add_vec:
                                next_p = (p[0]+add[0], p[1]+add[1])
                                if 0 <= next_p[0] < n and 0 <= next_p[1] < n and grid[next_p[0]][next_p[1]] == 1 and next_p not in visit:
                                    next_queue.add(next_p)

                        queue = None
                        if len(next_queue) > 0:
                            queue = next_queue
                    
                    one_visit |= visit
                    island.append(visit)
        
        # print(len(island))
        # print(island)

        count = 0
        visit = set()
        queue = island[0]
        while queue:
            next_queue = set()
            visit |= queue
            for p in queue:
                for add in add_vec:
                    next_p = (p[0]+add[0], p[1]+add[1])
                    if 0 <= next_p[0] < n and 0 <= next_p[1] < n and next_p not in visit:
                        next_queue.add(next_p)

            queue = None
            if len(next_queue) > 0:
                queue = next_queue
                count += 1
                for p in queue:
                    if p in island[1]:
                        return count - 1

        return -1