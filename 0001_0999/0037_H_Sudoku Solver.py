class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        strDigits = set([str(i) for i in range(1, 10)])
        rowDigits = [set() for _ in range(9)]
        columnDigits = [set() for _ in range(9)]
        boxDigits = [[set() for _ in range(3)] for _ in range(3)]
        emptyCells = []

        for y in range(9):
            for x in range(9):
                val = board[y][x]
                if val == '.':
                    emptyCells.append((y, x))
                else:
                    rowDigits[y].add(val)
                    columnDigits[x].add(val)
                    boxDigits[y//3][x//3].add(val)

        def DFS(i):
            if i == len(emptyCells):
                return True

            y, x = emptyCells[i]
            boxY, boxX = y//3, x//3
            thisDigits = strDigits - (rowDigits[y] | columnDigits[x] | boxDigits[boxY][boxX])
            for val in thisDigits:
                board[y][x] = val
                rowDigits[y].add(val)
                columnDigits[x].add(val)
                boxDigits[boxY][boxX].add(val)

                if DFS(i+1):
                    return True

                board[y][x] = '.'
                rowDigits[y].discard(val)
                columnDigits[x].discard(val)
                boxDigits[boxY][boxX].discard(val)

            return False

        DFS(0)