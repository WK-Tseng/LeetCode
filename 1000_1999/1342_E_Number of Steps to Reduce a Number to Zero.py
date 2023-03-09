class Solution:
    def numberOfSteps(self, num: int) -> int:
        bit_s = bin(num)[2:]
        return bit_s.count('1') * 2 + bit_s.count('0') - 1 