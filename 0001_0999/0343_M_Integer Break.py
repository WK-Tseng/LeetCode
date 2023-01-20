class Solution:
    def integerBreak(self, n: int) -> int:

        def try_sum(target, result):
            if target == 0:
                return
            elif target == 4:
                result.append(4)
                target -= 4
            elif target >= 3:
                result.append(3)
                target -= 3
            else:
                result.append(target)
                target = 0

            try_sum(target, result)

        if n == 2:
            return 1
        elif n == 3:
            return 2

        result = []
        try_sum(n, result)
        # print(result)
        product = 1
        for i in result:
            product *= i

        return product