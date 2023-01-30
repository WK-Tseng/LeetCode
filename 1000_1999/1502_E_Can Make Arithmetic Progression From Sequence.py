class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for idx, num in enumerate(arr[2:], 2):
            if diff != num - arr[idx-1]:
                return False

        return True