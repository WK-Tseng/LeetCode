class Solution:
    # AC, fast and low memory
    def numTilings(self, n: int) -> int:
        result = [1, 2, 5]

        if n <= 3:
            return result[n-1]

        for _ in range(3, n):
            result.append(result[-1] * 2 + result.pop(0))
        
        return result[-1] % (10**9 + 7)


    # AC, fast
    # def numTilings(self, n: int) -> int:
    #     result = [1, 2, 5] + [-1] * (n-3)

    #     for i in range(3, n):
    #         result[i] = result[i-1] * 2 + result[i-3]

    #     return result[n-1] % (10**9 + 7)