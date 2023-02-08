class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(maze), len(maze[0])

        exit_cell = set()
        for y in range(m):
            if maze[y][0] == '.':
                exit_cell.add((y, 0))
            if maze[y][n-1] == '.':
                exit_cell.add((y, n-1))

        for x in range(n):
            if maze[0][x] == '.':
                exit_cell.add((0, x))
            if maze[m-1][x] == '.':
                exit_cell.add((m-1, x))
        
        exit_cell.discard((entrance[0], entrance[1]))
        if len(exit_cell) == 0:
            return -1
        
        count = 0
        visit = set()
        queue = set()
        queue.add((entrance[0], entrance[1]))
        while queue:
            count += 1
            next_queue = set()
            visit |= queue
            for p in queue:
                for add in add_vec:
                    next_p = (p[0]+add[0], p[1]+add[1])
                    if 0 <= next_p[0] < m and 0 <= next_p[1] < n and maze[next_p[0]][next_p[1]] == '.' and next_p not in visit:
                        next_queue.add(next_p)
                        if next_p in exit_cell:
                            return count

            queue = None
            if len(next_queue) > 0:
                queue = next_queue
        
        return -1