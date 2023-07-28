class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        sign = '' if num >= 0 else '-'
        num = abs(num)

        base7 = []
        b7 = 7
        lastB7 = 1
        while num > 0:
            tmp = num % b7
            num -= tmp
            base7.append(str(tmp // lastB7))
            b7, lastB7 = b7*7, b7

        return sign + ''.join(base7[::-1])