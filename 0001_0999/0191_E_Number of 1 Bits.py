class Solution:
    def hammingWeight(self, n: int) -> int:
        
        nBit = list(bin(abs(n))[2:].zfill(32))

        if n < 0:
            flag = False
            for i in range(len(nBit)-1, -1, -1):
                if not flag:
                    if nBit[i] == '1':
                        flag = True
                else:
                    nBit[i] = '1' if nBit[i] == '0' else '0'
        
        count = 0
        for b in nBit:
            if b == '1':
                count += 1
        
        return count