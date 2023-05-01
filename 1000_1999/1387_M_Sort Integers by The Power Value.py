class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        data = {}
        result = []

        for i in range(lo, hi+1):
            times = 0
            n = i
            stack = []
            while n != 1:
                if n in data:
                    times += data[n]
                    n = 1
                else:
                    stack.append((n, 1))
                    times += 1
                    if n & 1:
                        n *= 3
                        n += 1
                    else:
                        n //= 2

            result.append((i, times))

            while stack:
                d, t = stack.pop(0)
                data[d] = times
                times -= t
            
        return sorted(result, key=lambda x:x[1])[k-1][0]