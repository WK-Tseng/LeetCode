class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        N = len(arr)
        result = 0

        for i in range(N):
            result += ((i+1) * (N-i) + 1) // 2 * arr[i]

        return result