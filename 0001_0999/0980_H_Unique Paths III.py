class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        add_vec = ((1, 0), (-1, 0), (0, 1), (0, -1),)

        start = None
        end = None
        empty_counter = 0

        for y in range(m):
            for x in range(n):
                val = grid[y][x]
                if val == 0:
                    empty_counter += 1
                if val == 1:
                    start = (y, x)
                elif val == 2:
                    end = (y, x)

        

        def DFS(point, counter=-1):
            result_times = 0
            val = grid[point[0]][point[1]]

            if val == 0 or val == 1:
                grid[point[0]][point[1]] = -2
                counter += 1

                for vec in add_vec:
                    next_point = (point[0] + vec[0], point[1] + vec[1])
                    if 0 <= next_point[0] < m and 0 <= next_point[1] < n:
                        result_times += DFS(next_point, counter)

                grid[point[0]][point[1]] = val
                
            elif val == 2:
                if counter == empty_counter:
                    result_times = 1
            
            return result_times

        return DFS(start)