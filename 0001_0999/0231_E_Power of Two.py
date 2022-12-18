class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
            
        nBin = bin(n)[2:]
        return nBin[0] == '1' and not(any(b == '1' for b in nBin[1:]))