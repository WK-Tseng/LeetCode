class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        numsLen = len(nums)
        ansList = []
        
        # print(nums)
        
        for i in range(numsLen-3):
            if i > 0:
                if nums[i] == nums[i-1]:
                    # print(i)
                    continue
            for d in range(i+1, numsLen-2):
                if d > i+1:
                    if nums[d] == nums[d-1]:
                        continue
                
                # print(f"{i}, {d}")
            
                j = d + 1
                k = numsLen - 1

                # print(j, k)

                # if j < k:
                while j < k:
                    val = nums[i] + nums[d] + nums[j] + nums[k]

                    if val == target:
                        ansList.append([nums[i], nums[d], nums[j], nums[k]])

                    if val > target:
                        while True:
                            k -= 1
                            if (not (j < k)) or k <= numsLen or nums[k] != nums[k+1]:
                                break

                    elif val <= target:
                        while True:
                            j += 1
                            if (not (j < k)) or j >= numsLen or nums[j] != nums[j-1]:
                                break
        
        return ansList