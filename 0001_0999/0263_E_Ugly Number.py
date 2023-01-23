class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1 or n == 0:
            return True if n else False
        else:
            flag = False
            for i in [2, 3, 5]:
                if n % i == 0:
                    flag |= self.isUgly(n//i)
                    if flag:
                        break

            return flag