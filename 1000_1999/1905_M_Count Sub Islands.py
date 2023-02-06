class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid2), len(grid2[0])

        one_visit2 = set()
        land2 = []

        for y in range(m):
            for x in range(n):
                point = (y, x)
                if grid2[y][x] == 1 and point not in one_visit2:
                    queue = set()
                    queue.add(point)
                    visit = set()
                    while queue:
                        visit |= queue
                        next_queue = set()
                        for p in queue:
                            for add in add_vec:
                                next_p = (p[0]+add[0], p[1]+add[1])
                                if 0 <= next_p[0] < m and 0 <= next_p[1] < n and grid2[next_p[0]][next_p[1]] == 1 and next_p not in visit:
                                    next_queue.add(next_p)

                        queue = None
                        if len(next_queue) > 0:
                            queue = next_queue

                    one_visit2 |= visit
                    land2.append(visit)

        # print(land2)

        sub_count = 0
        for land in land2:
            isSub = True
            for point in land:
                if grid1[point[0]][point[1]] == 0:
                    isSub = False
                    break
            
            if isSub:
                sub_count += 1

        return sub_count