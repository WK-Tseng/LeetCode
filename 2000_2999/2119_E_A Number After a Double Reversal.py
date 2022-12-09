class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        numStr = str(num)
        return numStr[-1] != '0'

    # AC
    # def isSameAfterReversals(self, num: int) -> bool:
    #     return num == 0 or num % 10 != 0