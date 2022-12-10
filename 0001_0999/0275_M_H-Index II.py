class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        citLen = len(citations)

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == citLen - mid:
                return citations[mid]
            elif citations[mid] > citLen - mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return citLen - (right + 1)