class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        end = n * n - 1
        line_board = []
        for idx, line in enumerate(board[::-1]):
            if idx % 2 == 1:
                line_board += line[::-1]
            else:
                line_board += line

        # print(line_board)

        count = 0
        visit = set()
        queue = set([0])

        while queue:
            next_queue = set()
            visit |= queue

            for p in queue:

                if line_board[p] != -1:
                    p = line_board[p] - 1

                if p == end:
                    return count
                
                for add in range(1, 7):
                    next_p = p + add

                    if next_p <= end and next_p not in visit:
                        next_queue.add(next_p)
            count += 1

            queue = None
            if len(next_queue) > 0:
                queue = next_queue
                
        return -1