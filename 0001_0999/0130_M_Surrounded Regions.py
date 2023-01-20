class Solution:
    # AC, fast
    def solve(self, board: List[List[str]]) -> None:
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])

        edge_O_point = set()

        for y in range(m):
            if board[y][0] == 'O':
                edge_O_point.add((y, 0))
            if board[y][n-1] == 'O':
                edge_O_point.add((y, n-1))

        for x in range(n):
            if board[0][x] == 'O':
                edge_O_point.add((0, x))
            if board[m-1][x] == 'O':
                edge_O_point.add((m-1, x))

        for try_point in edge_O_point:
            if board[try_point[0]][try_point[1]] == 'O':
                visit = set()
                queue = set([try_point])
                while queue:
                    visit |= queue
                    next_queue = set()
                    for p in queue:
                        for vec in add_vec:
                            next_p = (p[0] + vec[0], p[1] + vec[1])
                            if 0 <= next_p[0] < m and 0 <= next_p[1] < n and board[next_p[0]][next_p[1]] == 'O':
                                if next_p not in next_queue and next_p not in visit:
                                    next_queue.add(next_p)

                    queue = None
                    if len(next_queue) > 0:
                        queue = next_queue
                
                for p in visit:
                    board[p[0]][p[1]] = 'E'

        for y in range(m):
            for x in range(n):
                if board[y][x] == 'O':
                    board[y][x] = 'X'

        for y in range(m):
            for x in range(n):
                if board[y][x] == 'E':
                    board[y][x] = 'O'
                

    # AC, slow
    # def solve(self, board: List[List[str]]) -> None:
    #     add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     m, n = len(board), len(board[0])

    #     O_point = set([(y, x) for y in range(m) for x in range(n) if board[y][x] == 'O'])

    #     O_visit = set()
    #     for try_point in O_point:
    #         if try_point not in O_visit:
    #             visit = set()
    #             queue = set([try_point])
    #             while queue:
    #                 visit |= queue
    #                 next_queue = set()
    #                 for p in queue:
    #                     for vec in add_vec:
    #                         next_p = (p[0] + vec[0], p[1] + vec[1])
    #                         if next_p in O_point:
    #                             if next_p not in next_queue and next_p not in visit:
    #                                 next_queue.add(next_p)
    #                 queue = None
    #                 if len(next_queue) > 0:
    #                     queue = next_queue

    #             O_visit |= visit

    #             edge = any(p[0] == 0 or p[0] == m-1 or p[1] == 0 or p[1] == n-1 for p in visit)

    #             if not edge:
    #                 for p in visit:
    #                     board[p[0]][p[1]] = 'X'

    # AC, slow
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     m, n = len(board), len(board[0])
    #     # print(m, n)

    #     try_visit = set()

    #     for y in range(m):
    #         for x in range(n):
    #             if board[y][x] == 'O' and (y, x) not in try_visit:
    #                 visit = set()
    #                 queue = set([(y, x)])
    #                 while queue:
    #                     visit |= queue
    #                     next_queue = set()
    #                     for p in queue:
    #                         for vec in add_vec:
    #                             next_p = (p[0] + vec[0], p[1] + vec[1])
    #                             if 0 <= next_p[0] < m and 0 <= next_p[1] < n:
    #                                 if board[next_p[0]][next_p[1]] == 'O' and next_p not in next_queue and next_p not in visit:
    #                                     next_queue.add(next_p)
    #                     queue = None
    #                     if len(next_queue) > 0:
    #                         queue = next_queue
                    
    #                 try_visit |= visit

    #                 # print(visit)
    #                 # edge = False
    #                 # for p in visit:
    #                 #     if p[0] == 0 or p[0] == m-1 or p[1] == 0 or p[1] == n-1:
    #                 #         edge = True
    #                 #         break
    #                 edge = any(p[0] == 0 or p[0] == m-1 or p[1] == 0 or p[1] == n-1 for p in visit)
                    
    #                 if not edge:
    #                     for p in visit:
    #                         board[p[0]][p[1]] = 'X'
