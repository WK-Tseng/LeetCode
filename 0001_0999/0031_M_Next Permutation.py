class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        changeFlag = False

        for i in range(2, len(nums)+1):
            # print(nums[-i:])
            
            thisSlice = nums[-i:]
            if not (thisSlice[0] >= thisSlice[1]):
                # print('----', i, (-i)+1)
                flag = False
                for j in range((-i)+1, 0, 1):
                    # print('++++', j)
                    if nums[-i] >= nums[j]:
                        nums[-i], nums[j-1] = nums[j-1], nums[-i]
                        flag = True
                        break
                
                if not flag:
                    nums[-i], nums[-1] = nums[-1], nums[-i]

                nums[(-i)+1:] = sorted(nums[(-i)+1:])
                # print(nums[-i:])

                changeFlag = True
                break

        if not changeFlag:
            nums[:] = nums[::-1]

        
                