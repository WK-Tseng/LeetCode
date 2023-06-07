class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        aStr = bin(a)[2:]
        bStr = bin(b)[2:]
        cStr = bin(c)[2:]

        aN, bN, cN = len(aStr), len(bStr), len(cStr)
        maxN = max(aN, bN, cN)

        if aN < maxN:
            aStr = ('0' * (maxN-aN)) + aStr
        
        if bN < maxN:
            bStr = ('0' * (maxN-bN)) + bStr

        if cN < maxN:
            cStr = ('0' * (maxN-cN)) + cStr

        # print(aStr, bStr, cStr)

        for x, y, z in zip(aStr, bStr, cStr):
            if z == '0':
                if x == '1':
                    count += 1
                if y == '1':
                    count += 1

            else:
                if x == '0' and y == '0':
                    count += 1

            # print(x, y, z)


        return count