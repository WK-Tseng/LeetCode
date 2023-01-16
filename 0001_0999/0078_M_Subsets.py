class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = []

        def DFS(temp, i):
            if i == N:
                # print(temp)
                result.append([n for n in temp])
                return

            DFS(temp, i+1)
            
            temp.append(nums[i])
            DFS(temp, i+1)
            temp.pop(-1)

        DFS([], 0)
        return result