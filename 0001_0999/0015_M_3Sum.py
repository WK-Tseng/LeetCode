class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        numsLen = len(nums)
        ansList = []
        
        # print(nums)
        
        for i in range(numsLen-2):
            if i > 0:
                if nums[i] == nums[i-1]:
                    # print(i)
                    continue
            
            j = i + 1
            k = numsLen - 1
            
            # print(j, k)
            
            # if j < k:
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                
                if val == 0:
                    ansList.append([nums[i], nums[j], nums[k]])
                
                if val > 0:
                    while True:
                        k -= 1
                        if (not (j < k)) or k <= numsLen or nums[k] != nums[k+1]:
                            break
                
                elif val <= 0:
                    while True:
                        j += 1
                        if (not (j < k)) or j >= numsLen or nums[j] != nums[j-1]:
                            break
        
        return ansList