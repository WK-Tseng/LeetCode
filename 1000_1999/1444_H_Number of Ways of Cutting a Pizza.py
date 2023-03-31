class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        @cache
        def hasApple(r1, c1, r2, c2):
            return any(pizza[r][c] == 'A' for c in range(c1, c2+1) for r in range(r1, r2+1))

        @cache
        def dp(r, c, life):

            if life == 1:
                if hasApple(r, c, m-1, n-1):
                    return 1

            result = 0
            for y in range(r+1, m):
                if hasApple(r, c, y-1, n-1):
                    result += dp(y, c, life-1)

            for x in range(c+1, n):
                if hasApple(r, c, m-1, x-1):
                    result += dp(r, x, life-1)

            return result

        return dp(0, 0, k) % (10**9 + 7)