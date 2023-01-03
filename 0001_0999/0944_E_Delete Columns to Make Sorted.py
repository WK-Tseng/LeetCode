class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])

        delete_count = 0

        for x in range(n):
            first = strs[0][x]
            for y in range(1, m):
                this = strs[y][x]
                if this < first:
                    delete_count += 1
                    break
                first = this

        return delete_count