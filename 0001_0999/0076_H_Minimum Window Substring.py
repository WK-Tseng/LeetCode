class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = Counter(t)
        miss_count = len(t)

        temp_start = 0
        start, end = 0, 0
        for i, c in enumerate(s, 1): # i start 1

            miss_count -= (t_count[c] > 0)
            t_count[c] -= 1
            
            if miss_count == 0:
                _c = s[temp_start]
                while temp_start < i and t_count[_c] < 0:
                    t_count[_c] += 1
                    temp_start += 1
                    _c = s[temp_start]
                    
                if end == 0 or i - temp_start <= end - start:
                    start, end = temp_start, i

        return s[start:end]