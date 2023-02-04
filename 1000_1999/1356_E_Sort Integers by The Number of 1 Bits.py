class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [data[1] for data in sorted((bin(n)[2:].count('1'), n) for n in arr)]