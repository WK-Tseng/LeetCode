class Solution:
    # AC, fast
    def minPartitions(self, n: str) -> int:
        return int(max(n))

    # AC, slow
    # def minPartitions(self, n: str) -> int:
    #     return max(int(c) for c in n)

    # AC, slow
    # def minPartitions(self, n: str) -> int:
    #     result = -1
    #     for c in n:
    #         result = max(result, int(c))
    #     return result