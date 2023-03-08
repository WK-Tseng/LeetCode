class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            # count = 0
            # for p in piles:
            #     count += (p // mid) + ((p % mid) != 0)
            count = sum(((p // mid) + ((p % mid) != 0)) for p in piles)
                
            if count > h:
                left = mid + 1
            else:
                right = mid

        return left
            