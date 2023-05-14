class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        nn = n // 2
        
        @cache
        def gcd(x, y):
            return math.gcd(x, y)

        @cache
        def dfs(idx, mask):
            if idx > nn:
                return 0
            
            result = 0
            for i in range(n):
                for j in range(i+1, n):
                    tempMask = (1 << i) | (1 << j)
                    if not mask & tempMask:
                        result = max(result, idx * gcd(nums[i], nums[j]) + dfs(idx+1, mask | tempMask))

            return result
        
        return dfs(1, 0)