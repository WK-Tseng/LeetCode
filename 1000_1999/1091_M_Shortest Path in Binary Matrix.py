class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        add_vec = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        N = len(grid)
        target = (N-1, N-1)

        visit = set()
        queue = set()
        count = 0
        target_find = False

        if grid[0][0] == 0:
            queue.add((0, 0))
            if N == 1:
                return 1

        while queue and not target_find:
            # print('------')
            count += 1
            visit |= queue
            next_queue = set()
            for p in queue:
                for vec in add_vec:
                    next_p = (p[0] + vec[0], p[1] + vec[1])
                    if 0 <= next_p[0] < N and 0 <= next_p[1] < N:
                        if grid[next_p[0]][next_p[1]] == 0 and next_p not in next_queue and next_p not in visit:
                            next_queue.add(next_p)
                            # print(next_p)
                            if next_p == target:
                                target_find = True
                                return count + 1

            queue = None
            if len(next_queue) > 0:
                queue = next_queue
        
        return -1
            
