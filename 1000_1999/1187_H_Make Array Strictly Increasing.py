class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        arr2 = sorted(set(arr2))

        @cache
        def DFS(i, prev):
            if i >= len(arr1):
                return 0
            
            j = bisect.bisect_right(arr2, prev)
            swap = (1 + DFS(i+1, arr2[j])) if j < len(arr2) else float('inf')
            noSwap = DFS(i+1, arr1[i]) if arr1[i] > prev else float('inf')
            return min(swap, noSwap)

        result = DFS(0, float('-inf'))
        return result if result != float('inf') else -1