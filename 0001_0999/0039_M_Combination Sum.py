class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []

        def DFS(data, t):
            if t < 0:
                return
            elif t == 0:
                result.append([n for n in temp])
                return

            for i in range(len(data)):
                temp.append(data[i])
                DFS(data[i:], t - data[i])
                temp[:] = temp[:-1]

        DFS(candidates, target)

        return result