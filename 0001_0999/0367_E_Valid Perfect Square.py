class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left + 1 != right:
            mid = (left + right) // 2
            n = mid ** 2

            if n == num:
                return True
            elif n > num:
                right = mid
            else:
                left = mid
            
        return False