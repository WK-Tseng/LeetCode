class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        numsLen = len(nums)
        
        nowVal = nums[0] + nums[1] + nums[2]
        diff = abs(nowVal - target)
        
        # print(nums)
        
        for i in range(numsLen-2):
            if i > 0:
                if nums[i] == nums[i-1]:
                    # print(i)
                    continue
            
            j = i + 1
            k = numsLen - 1
            
            # print(j, k)
            
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                thisDiff = abs(val - target)
                
                if thisDiff < diff:
                    nowVal = val
                    diff = thisDiff
                    
                    if diff == 0:
                        break
                
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
                            
            if diff == 0:
                break
        
        return nowVal