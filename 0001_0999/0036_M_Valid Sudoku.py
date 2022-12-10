class Solution:
    # AC
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # row
            if not all(v == 1 for k, v in Counter(board[i]).items() if k != '.'):
                return False

            # column
            if not all(v == 1 for k, v in Counter([board[j][i] for j in range(9)]).items() if k != '.'):
                return False

            # matrix            
            if not all(v == 1 for k, v in Counter([board[(i%3)*3 + j%3][(i//3)*3 + j//3] for j in range(9)]).items() if k != '.'):
                return False

        return True
    
    # AC
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     for i in range(9):
    #         # row
    #         if max([v for k, v in Counter(board[i]).items() if k != '.'] or [1]) != 1:
    #             return False

    #         # column
    #         if max([v for k, v in Counter([board[j][i] for j in range(9)]).items() if k != '.'] or [1]) != 1:
    #             return False

    #         # matrix
    #         if max([v for k, v in Counter([board[(i%3)*3 + j%3][(i//3)*3 + j//3] for j in range(9)]).items() if k != '.'] or [1]) != 1:
    #             return False

    #     return True

    # AC
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     matrixSets = [[set() for _ in range(3)] for _ in range(3)]

    #     rowSet = set()
    #     columnSet = set()

    #     for i in range(9):
    #         rowSet.clear()
    #         columnSet.clear()
    #         for j in range(9):
    #             rowVal = board[i][j]
    #             if rowVal != '.':
    #                 if rowVal in rowSet:
    #                     return False
    #                 else:
    #                     rowSet.add(rowVal)

    #             columnVal = board[j][i]
    #             if columnVal != '.':
    #                 if columnVal in columnSet:
    #                     return False
    #                 else:
    #                     columnSet.add(columnVal)

    #             matrixVal = rowVal
    #             if matrixVal != '.':
    #                 if matrixVal in matrixSets[i//3][j//3]:
    #                     return False
    #                 else:
    #                     matrixSets[i//3][j//3].add(matrixVal)

    #     return True

    # AC
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rowSets = [set() for _ in range(9)] 
    #     columnSets = [set() for _ in range(9)]
    #     matrixSets = [[set() for _ in range(3)] for _ in range(3)]

    #     for i in range(9):
    #         for j in range(9):
    #             val = board[i][j]
    #             if val != '.':
    #                 if val in rowSets[i]:
    #                     return False
    #                 else:
    #                     rowSets[i].add(val)

    #                 if val in columnSets[j]:
    #                     return False
    #                 else:
    #                     columnSets[j].add(val)

    #                 if val in matrixSets[i//3][j//3]:
    #                     return False
    #                 else:
    #                     matrixSets[i//3][j//3].add(val)

    #     return True