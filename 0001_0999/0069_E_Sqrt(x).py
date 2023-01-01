class Solution:
    # AC, fast
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        
        left, right =  0, x // 2
        mid = (left + right) // 2

        while left <= right:
            mid = (left + right) // 2
            val = mid**2
            if val == x:
                return mid
            elif val > x:
                right = mid - 1
            else:
                left = mid + 1

        if mid**2 > x:
            return mid - 1
        else:   
            return mid



    # AC, slow
    # def mySqrt(self, x: int) -> int:
    #     result = 1

    #     while result**2 <= x:
    #         result += 1

    #     return result - 1