class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        
        k_left = int(log(left, 2))
        k_right = int(log(right, 2))

        if k_left != k_right:
            return 0
        else:
            temp = 2**k_left
            return temp | self.rangeBitwiseAnd(left-temp, right-temp)
