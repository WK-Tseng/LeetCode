class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_ocean = 0b01
        atlantic_ocean = 0b10
        target = pacific_ocean | atlantic_ocean
        
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m, n = len(heights), len(heights[0])
        result_2D_map = [[0]*n for _ in range(m)]

        result = set()

        def BFS(y, x, ocean):
            if result_2D_map[y][x] & ocean != 0:
                return

            queue = set([(y,x)])
            while queue:
                # print(queue)
                next_queue = set()
                for point in queue:
                    result_2D_map[point[0]][point[1]] |= ocean
                    _height = heights[point[0]][point[1]]

                    if result_2D_map[point[0]][point[1]] == target:
                        result.add(point)

                    for vec in add_vec:
                        next_point = (point[0] + vec[0], point[1] + vec[1])

                        if 0 <= next_point[0] < m and 0 <= next_point[1] < n and \
                        heights[next_point[0]][next_point[1]] >= _height and \
                        result_2D_map[next_point[0]][next_point[1]] & ocean == 0:
                            next_queue.add(next_point)

                queue = None
                if len(next_queue) > 0:
                    queue = next_queue


        for x in range(n):
            BFS(0, x, pacific_ocean)
            BFS(m-1, x, atlantic_ocean)

        # print('--------------')
        # for r in result_2D_map:
        #     print(r)

        for y in range(m):
            BFS(y, 0, pacific_ocean)
            BFS(y, n-1, atlantic_ocean)

        # print('--------------')
        # for r in result_2D_map:
        #     print(r)

        return result