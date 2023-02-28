class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = num % 10
            num //= 10
            num += temp
        return num

    # AC, slow
    # def addDigits(self, num: int) -> int:
    #     if num < 10:
    #         return num

    #     addNums = 0
    #     while num:
    #         addNums += num % 10
    #         num //= 10
    #     return self.addDigits(addNums)

    # AC, slow
    # def addDigits(self, num: int) -> int:
    #     if num < 10:
    #         return num

    #     addNums = 0
    #     for ns in str(num):
    #         addNums += int(ns)
    #     return self.addDigits(addNums)