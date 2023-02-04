class NumArray:
    def __init__(self, nums: List[int]):
        self.sum_nums = [0]
        ss = 0
        for n in nums:
            ss += n
            self.sum_nums.append(ss)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_nums[right+1] - self.sum_nums[left]


    # AC, slow
    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     return sum(self.nums[left:right+1])
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)