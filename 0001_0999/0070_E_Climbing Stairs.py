class Solution:
    # AC, slow, but uses very little memory.
    # def climbStairs(self, n: int) -> int:
    #     lastTwo, lastOne = 1, 2
    #     for i in range(n-2):
    #         lastTwo, lastOne = lastOne, lastTwo + lastOne

    #     return lastOne if n > 1 else lastTwo

    # AC, fast, but uses too much memory.
    def climbStairs(self, n: int) -> int:
        result = [0, 1, 2]
        resultLen = len(result)

        for i in range(resultLen, n + 1):
            result.append(result[i-2] + result[i-1])
        
        return result[n]