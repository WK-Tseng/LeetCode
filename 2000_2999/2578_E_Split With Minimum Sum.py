class Solution:
    def splitNum(self, num: int) -> int:
        num_s = list(str(num))
        num_s.sort()
        num_s = num_s[::-1]

        result = 0
        count = 0
        d = 1
        for i in range(len(num_s)):
            result += int(num_s[i]) * d
            count += 1
            if count == 2:
                count = 0
                d *= 10

        return result