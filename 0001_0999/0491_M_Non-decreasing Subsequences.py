class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        results = set()

        def search_sub(i, result = []):
            if i < N:

                # take
                take_flag = False
                if len(result) == 0:
                    result.append(nums[i])
                    take_flag = True

                elif nums[i] >= result[-1]:
                    result.append(nums[i])
                    take_flag = True
                    results.add(tuple(result))

                search_sub(i+1, result)

                # not take
                if take_flag:
                    result.pop(-1)
                    search_sub(i+1, result)
        
        search_sub(0)

        return results