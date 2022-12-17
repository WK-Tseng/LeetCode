class Solution:
    # def multiply(self, num1: str, num2: str) -> str:
    #     return str(int(num1) * int(num2))

    # def multiply(self, num1: str, num2: str) -> str:
    #     numlist1 = [int(n) for n in num1]
    #     numlist2 = [int(n) for n in num2]
    #     len1, len2 = len(num1), len(num2)
    #     ans = 0

    #     for i in range(len1):
    #         for j in range(len2):
    #             ans += numlist1[i] * (10**(len1-i-1)) * numlist2[j] * (10**(len2-j-1))

    #     return str(ans)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        numList1 = [int(n) for n in num1][::-1]
        numList2 = [int(n) for n in num2][::-1]
        len1, len2 = len(num1), len(num2)

        resultList = [0] *  (len1 + len2 + 1)

        for i in range(len1):
            for j in range(len2):
                temp = numList1[i] * numList2[j]
                resultList[i+j] += temp

        for i in range(len(resultList) - 1):
            temp = resultList[i]
            if temp >= 10:
                resultList[i] = temp % 10
                resultList[i+1] += temp // 10

        resultList[:] = resultList[::-1]
        for i in range(len(resultList)):
            if resultList[i] != 0:
                resultList[:] = [str(j) for j in resultList[i:]] or ['0']
                break

        return ''.join(resultList)