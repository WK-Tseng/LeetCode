class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def result(idx, m, player):
            if idx < len(piles):
                if player:
                    return max([sum(piles[idx:idx+x]) + result(idx+x, max(m,x), not player) for x in range(1, 2*m+1)])
                else:
                    return min([result(idx+x, max(m,x), not player) for x in range(1, 2*m+1)])
            else:
                return 0

        return result(0, 1, True)