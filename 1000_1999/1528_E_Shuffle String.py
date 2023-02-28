class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i, j in enumerate(indices):
            result[j] = s[i]
        return ''.join(result)