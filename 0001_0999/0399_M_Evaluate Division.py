class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            graph[a][b] = v
            graph[b][a] = 1.0/v

        result = []
        for a, b in queries:
            queue = [(a, 1)]
            visit = set()
            tempResult = -1.0
            while queue:
                t, v = queue.pop(0)
                visit.add(t)

                if t == b and t in graph:
                    tempResult = v
                    break

                for n in graph[t]:
                    if n not in visit:
                        queue.append((n, v*graph[t][n]))

            result.append(tempResult)

        return result
            

        