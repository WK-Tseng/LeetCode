class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        # data = [(sum(m), i) for i, m in enumerate(mat)]
        # data.sort(key=lambda x: x)
        # return [i[1] for i in data[:k]]

        return [i[1] for i in sorted([(sum(m), i) for i, m in enumerate(mat)], key=lambda x: x)[:k]]