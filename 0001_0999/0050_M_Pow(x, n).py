class Solution:
    # AC, fast
    # def myPow(self, x: float, n: int) -> float:
    #     return x**n

    # AC, Implement pow
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)

        resultDict = {}
        resultDict[0] = 1
        resultDict[1] = x

        def Pow(n):
            if n not in resultDict:
                r = n // 2
                result = Pow(r) * Pow(n - r)
                resultDict[n] = result
                return result
            else:
                return resultDict[n]

        return Pow(n)

    # MemoryError
    # x = -1.00000, n = -2147483648
    # x = 1.00001, n = 123456
    # def myPow(self, x: float, n: int) -> float:
    #     if n < 0:
    #         x = 1/x
    #         n = abs(n)

    #     if n == 0:
    #         return 1

        
    #     result = [x] * n
    #     while len(result) > 1:
    #         resultLen = len(result)
    #         result = [result[i]*result[i+1] if i+1 < resultLen else result[i] for i in range(0, resultLen, 2)]
            
    #     return result[0]

