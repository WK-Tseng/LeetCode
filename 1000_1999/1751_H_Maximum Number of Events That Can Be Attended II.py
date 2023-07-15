class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort(key=lambda x:x[0])
        eventsLen = len(events)
        dp = [[-1]*(k+1) for _ in range(eventsLen)]

        def solve(i, k, end):
            if i == eventsLen:
                return 0
            
            if k == 0:
                return 0

            if events[i][0] <= end:
                return solve(i+1, k, end)

            if dp[i][k] != -1:
                return dp[i][k]

            select = max(events[i][2] + solve(i+1, k-1, events[i][1]), solve(i+1, k, end))
            dp[i][k] = select
            return select

        return solve(0, k, 0)