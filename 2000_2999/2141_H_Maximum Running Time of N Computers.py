class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        sumBat = sum(batteries)

        # 最大值足夠一台電腦從頭用到尾，因此扣掉
        while batteries[-1] > sumBat / n:
            n -= 1
            sumBat -= batteries.pop()

        return sumBat // n