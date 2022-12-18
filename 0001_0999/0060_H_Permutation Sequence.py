class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nList = [1] * (n-1)
        for i in range(1, (n-1)):
            nList[i] = nList[i-1] * (i+1)

        nList = [1] + nList
        # print(nList)

        nSet = list(range(1, n+1))
        result = ''
        for _ in range(n):
            factorial = nList.pop(-1)
            result += str(nSet.pop((k-1) // factorial))
            k %= factorial

        return result