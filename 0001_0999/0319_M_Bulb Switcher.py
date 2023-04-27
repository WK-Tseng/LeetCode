class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 因數為偶數則為亮，經統計猜測 N 開平方根取整數為答案
        return int(n**0.5)


    # timeout
    # def bulbSwitch(self, n: int) -> int:
    #     bulb = [False] * n
    #     for i in range(n):
    #         for j in range(i, n, i+1):
    #             bulb[j] = not bulb[j]

    #     return sum(bulb)