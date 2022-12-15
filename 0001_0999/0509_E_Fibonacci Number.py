class Solution:
    # AC, fast
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        Fn = [0, 1]
        for _ in range(n-1):
            Fn[0], Fn[1] = Fn[1], Fn[0] + Fn[1]
        return Fn[1]

    # AC
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return self.fib(n-1) + self.fib(n-2)

    # AC
    # def fib(self, n: int) -> int:
    #     return 0 if n == 0 else 1 if n == 1 else self.fib(n-1) + self.fib(n-2)