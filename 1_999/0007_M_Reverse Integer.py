class Solution:
    def reverse(self, x: int) -> int:
        sign = "-" if x < 0 else ""
        numStr = str(abs(x))
        
        for i in range(len(numStr)-1, -1, -1):
            if numStr[i] == '0':
                numStr = numStr.removesuffix('0')
            else:
                break
        
        numStr = sign + numStr[::-1]
        if numStr == '':
            numStr = '0'
        
        limt = 1 << 31
        
        if not ((-limt) <= int(numStr) <= (limt - 1)):
            numStr = '0'
        
        return numStr
        