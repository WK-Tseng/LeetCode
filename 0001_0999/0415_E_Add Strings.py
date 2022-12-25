class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        resultLen = max(len(num1), len(num2))
        num1 = num1.zfill(resultLen)
        num2 = num2.zfill(resultLen)

        result = []
        for n1, n2 in zip(num1, num2):
            result.append(int(n1) + int(n2))
        result.insert(0, 0)

        for i in range(len(result)-1, -1, -1):
            val = result[i]
            result[i-1] += val // 10
            result[i] = val % 10
            
        return str(int(''.join([str(n) for n in result])))