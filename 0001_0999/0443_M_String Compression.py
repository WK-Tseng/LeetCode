class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0
        times = 1
        for i, c in enumerate(chars[1:], 1):
            if c == chars[k]:
                times += 1
            else:
                if times > 1:
                    for t in str(times):
                        k += 1
                        chars[k] = t
                k += 1
                chars[k] = c
                times = 1
        
        if times > 1:
            for t in str(times):
                k += 1
                chars[k] = t

        return k+1