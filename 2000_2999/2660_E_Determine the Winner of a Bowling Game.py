class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        isTen1, wasTen1 = False, False
        isTen2, wasTen2 = False, False
        diff = 0

        for n1, n2 in zip(player1, player2):
            diff += (1 + (isTen1 | wasTen1)) * n1 - (1 + (isTen2 | wasTen2)) * n2

            isTen1, wasTen1 = n1 == 10, isTen1
            isTen2, wasTen2 = n2 == 10, isTen2

        return 1 if diff > 0 else 0 if diff == 0 else 2