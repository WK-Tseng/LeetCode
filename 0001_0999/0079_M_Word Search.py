class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        add_vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        N = len(word)

        def DFS(point, visit, i):
            
            result = False

            if board[point[0]][point[1]] == word[i] and i <= N-1:
                visit.add(point)
                # print(point, visit)
                if i == N-1:
                    # print('----------', visit)
                    return True

                for vec in add_vec:
                    next_p = (point[0] + vec[0], point[1] + vec[1])
                    if 0 <= next_p[0] < m and 0 <= next_p[1] < n and not result:
                        if next_p not in visit:
                            result |= DFS(next_p, visit, i+1)
                
                visit.remove(point)

            return result
        
        for y in range(m):
            for x in range(n):
                result = DFS((y, x), set(), 0)
                if result:
                    return True

        return False