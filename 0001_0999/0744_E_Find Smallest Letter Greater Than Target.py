class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            val = letters[mid]
            if val <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left if left < n else 0]