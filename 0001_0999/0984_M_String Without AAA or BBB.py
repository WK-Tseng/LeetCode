class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == 0 or b == 0:
            return 'a' * a + 'b' * b

        if a == b:
            return 'ab' * a

        if a > b:
            return 'aab' + self.strWithout3a3b(a - 2, b - 1)

        return self.strWithout3a3b(a - 1, b - 2) + 'abb'