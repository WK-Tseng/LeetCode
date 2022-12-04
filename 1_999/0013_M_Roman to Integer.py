class Solution:
    def romanToIntSlice(self, symbol, step, s):
        ans = 0
            
        if symbol[0] in s:
            idx = s.index(symbol[0])
            ans += (step * (10 - idx))
            s = s[idx+1:]
            
        elif symbol[1] in s:
            idx = s.index(symbol[1])
            ans += (step * 5)
            
            if idx == 0:
                s = s[1:]
                if len(s) != 0:
                    while s[0] == symbol[2]:
                        ans += step
                        s = s[1:]

                        if len(s) == 0:
                            break
            else:
                ans -= (step * idx)
                s = s[idx+1:]
        elif symbol[2] in s:
            while s[0] == symbol[2]:
                ans += step
                s = s[1:]
                
                if len(s) == 0:
                    break
        
        
        return ans, s
        
    
    def romanToInt(self, s: str) -> int:
        s = list(s)
        ans = 0
        
        while s[0] == 'M':
            ans += 1000
            s = s[1:]
            
            if len(s) == 0:
                break
            
        temp, s = self.romanToIntSlice(['M', 'D', 'C'], 100, s)
        ans += temp
        
        temp, s = self.romanToIntSlice(['C', 'L', 'X'], 10, s)
        ans += temp
        
        temp, s = self.romanToIntSlice(['X', 'V', 'I'], 1, s)
        ans += temp
            
        return ans