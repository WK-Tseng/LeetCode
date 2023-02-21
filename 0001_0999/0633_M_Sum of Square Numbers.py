class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            # fast
            s = a*a + b*b
            # slow
            # s = a**2 + b**2
            # print(a, b, s, c)
            if s == c:
                return True
            elif s > c:
                b -= 1
            else:
                a += 1

        return False