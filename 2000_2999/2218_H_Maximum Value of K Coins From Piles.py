class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for j, pile in enumerate(piles):
            s = pile[0]
            for i, _ in enumerate(pile[1:], 1):
                pile[i] += pile[i-1]
            
            piles[j] = pile[:k]

        pilesLen = len(piles)

        @lru_cache(None)
        def dp(pilesIdx, k):
            if k == 0 or pilesIdx == pilesLen:
                return 0
            nextIdx = pilesIdx + 1
            result = dp(nextIdx, k)
            for i, n in enumerate(piles[pilesIdx][:k]):
                result = max(result, n + dp(nextIdx, k-(i+1)))
            return result

        return dp(0, k)

       