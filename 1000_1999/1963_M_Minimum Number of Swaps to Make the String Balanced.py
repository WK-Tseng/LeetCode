class Solution:
    def minSwaps(self, s: str) -> int:
        balanced = 0
        result = 0
        for c in s:
            if c == '[':
                balanced += 1
            else:
                balanced -= 1
            result = min(result, balanced)
        return (-result + 1) // 2