class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return len(arr1) - sum(any(abs(n1 - n2) <= d for n2 in arr2) for n1 in arr1)