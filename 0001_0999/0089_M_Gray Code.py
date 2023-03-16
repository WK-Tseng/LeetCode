class Solution:
    def grayCode(self, n: int) -> List[int]:
        data = ['0', '1']
        for _ in range(1, n):
            data = ['0'+ d for d in data] + ['1'+ d for d in data[::-1]]

        return [int(d, 2) for d in data]