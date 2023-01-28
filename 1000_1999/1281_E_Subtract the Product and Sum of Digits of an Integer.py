class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        for c in str(n):
            n = int(c)
            s += n
            p *= n
        return p - s