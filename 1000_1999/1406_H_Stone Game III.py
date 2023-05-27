class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        data = collections.defaultdict(lambda: float('-inf'))

        @cache
        def dfs(idx):
            if idx >= n:
                return 0
            
            if idx in data:
                return data[idx]
            
            score = 0
            for i in range(idx, min(n, idx+3)):
                score += stoneValue[i]
                data[idx] = max(data[idx], score - dfs(i+1))

            return data[idx]

        result = dfs(0)
        return 'Tie' if result == 0 else 'Alice' if result > 0 else 'Bob'