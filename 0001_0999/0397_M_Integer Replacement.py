class Solution:
    def integerReplacement(self, n: int) -> int:
        
        data = {1:0}

        def func(n):
            if n in data:
                return data[n]

            if n & 1 == 0:
                data[n] = 1 + func(n//2)
                return data[n]
            
            n1, n2 = func(n+1), func(n-1)
            data[n] = 1 + min(n1, n2)
            return data[n]
        
        return func(n)

    # AC, slow
    # def integerReplacement(self, n: int) -> int:
    #     if n == 1:
    #         return 0
        
    #     if n & 1 == 0:
    #         return 1 + self.integerReplacement(n//2)
        
    #     n1, n2 = self.integerReplacement(n+1), self.integerReplacement(n-1)
    #     return 1 + min(n1, n2)