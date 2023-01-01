class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            c = digits[i] // 10
            digits[i] %= 10
            if c > 0:
                if i - 1 >= 0:
                    digits[i-1] += 1
                else:
                    digits.insert(0, 1)
        
        return digits