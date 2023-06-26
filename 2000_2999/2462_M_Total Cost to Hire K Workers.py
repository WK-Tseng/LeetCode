class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        idx1, idx2 = 0, len(costs)-1
        h1, h2 = [], []

        result = 0
        for _ in range(k):

            while len(h1) < candidates and idx1 <= idx2:
                heapq.heappush(h1, costs[idx1])
                idx1 += 1
            
            while len(h2) < candidates and idx1 <= idx2:
                heapq.heappush(h2, costs[idx2])
                idx2 -= 1

            a = h1[0] if h1 else float('inf')
            b = h2[0] if h2 else float('inf')

            if a <= b:
                result += a
                heapq.heappop(h1)
            else:
                result += b
                heapq.heappop(h2)
            
        return result