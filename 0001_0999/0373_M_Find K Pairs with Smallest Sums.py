class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m, n = len(nums1), len(nums2)

        result = []

        queue = [(nums1[0] + nums2[0], (0, 0))]
        visit = set()

        while len(result) < k and queue:
            _, (i, j) = heapq.heappop(queue)
            result.append((nums1[i], nums2[j]))

            next_j = j + 1
            nextPoint = (i, next_j)
            if next_j < n and nextPoint not in visit:
                heapq.heappush(queue, (nums1[i] + nums2[next_j], nextPoint))
                visit.add(nextPoint)

            next_i = i + 1
            nextPoint = (next_i, j)
            if next_i < m and (next_i, j) not in visit:
                heapq.heappush(queue, (nums1[next_i] + nums2[j], (next_i, j)))
                visit.add((next_i, j))

        return result