class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [1]
        idx2, idx3, idx5 = 0, 0, 0

        for _ in range(n-1):
            ugly2 = result[idx2] * 2
            ugly3 = result[idx3] * 3
            ugly5 = result[idx5] * 5
            next_ugly = min(ugly2, ugly3, ugly5)

            result.append(next_ugly)

            if next_ugly == ugly2:
                idx2 += 1

            if next_ugly == ugly3:
                idx3 += 1

            if next_ugly == ugly5:
                idx5 += 1

        # print(result)

        return result[-1]


    # AC, slow
    # def nthUglyNumber(self, n: int) -> int:
    #     result = [1]
    #     ugly_set = set()
    #     while len(result) < n:
    #         for i in [2, 3, 5]:
    #             ugly_set.add(result[-1]*i)
    #         min_ugly = min(ugly_set)

    #         result.append(min_ugly)
    #         ugly_set.remove(min_ugly)

    #     # print(result)
    #     return result[-1]