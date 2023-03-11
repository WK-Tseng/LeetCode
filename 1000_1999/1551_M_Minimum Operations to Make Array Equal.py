class Solution:
    # 等差級數
    def minOperations(self, n: int) -> int:
        if n & 1:
            count = n - 1
            result = (2 + count) * (count // 2) // 2
            return result
        else:
            count = n
            result = count // 2
            count -= 2
            result += (2 + count) * (count // 2) // 2
            return result

    # def minOperations(self, n: int) -> int:

    #     if n & 1:
    #         count = n - 1
    #         result = 0
    #         while count:
    #             result += count
    #             count -= 2
    #         return result
    #     else:
    #         count = n
    #         result = count // 2
    #         count -= 2
    #         while count:
    #             result += count
    #             count -= 2
    #         return result
        