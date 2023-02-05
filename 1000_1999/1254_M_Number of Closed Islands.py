class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        count = 0
        zero_visit = set()

        for y in range(m):
            for x in range(n):
                point = (y, x)
                if grid[y][x] == 0 and point not in zero_visit:
                    island = True
                    queue = set()
                    queue.add(point)
                    visit = set()
                    while queue:
                        visit |= queue
                        next_queue = set()
                        for p in queue:
                            for add in add_vec:
                                next_p = (p[0]+add[0], p[1]+add[1])
                                if 0 <= next_p[0] < m and 0 <= next_p[1] < n:
                                    if grid[next_p[0]][next_p[1]] == 0 and next_p not in visit:
                                        next_queue.add(next_p)
                                else:
                                    island = False
                        
                        queue = None
                        if len(next_queue) > 0:
                            queue = next_queue
                    
                    
                    zero_visit |= visit
                    if island:
                        count += 1
                    
        return count
