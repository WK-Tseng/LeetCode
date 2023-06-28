class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        path = collections.defaultdict(dict)
        for (a, b), p in zip(edges, succProb):
            path[a][b] = p
            path[b][a] = p

        result = [0] * n
        result[start] = 1

        queue = [start]

        while queue:
            point = queue.pop(0)
            thisP = result[point]
            data = path[point]
            for idx in data:
                tempP = thisP * data[idx]
                if tempP > result[idx]:
                    result[idx] = tempP
                    queue.append(idx)
        # print(path)

        return result[end]