class Solution:
    def myAtoi(self, s: str) -> int:
        Idx_1, Idx_2 = -1, -1
        
        chr_0 = ord('0')
        chr_9 = ord('9')
        
        Idx = 0
        
        for c in s:
            if Idx_1 == -1:
                if c == '-' or c == '+' or (chr_0 <= ord(c) <= chr_9):
                    Idx_1 = Idx
                elif c == ' ':
                    pass
                else:
                    return 0
            else:
                if chr_0 <= ord(c) <= chr_9:
                    Idx_2 = Idx
                else:
                    break
            
            Idx += 1
        
        if Idx_1 != -1:
            ans = s[Idx_1]
            if Idx_2 != -1:
                ans = s[Idx_1: Idx_2+1]
                
            try:
                ans = int(ans)
            except:
                return 0
            
                
            limt = 1 << 31
            if ans <= (-limt):
                ans = -limt
            elif ans >= (limt-1):
                ans = (limt-1)

            return ans
        else:
            return 0