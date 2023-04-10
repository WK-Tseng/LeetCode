class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegrees[v] += 1
        zero_indegree = set(i for i in range(n) if indegrees[i] == 0)
        counts = [defaultdict(int) for _ in range(n)]
        for i, c in enumerate(colors):
            counts[i][c] += 1
        max_count, visited = 0, 0
        while zero_indegree:
            u = zero_indegree.pop()
            visited += 1
            for v in graph[u]:
                for c in counts[u]:
                    counts[v][c] = max(counts[v][c], counts[u][c] + (colors[v] == c))
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    zero_indegree.add(v)
            max_count = max(max_count, max(counts[u].values()))
        return max_count if visited == n else -1