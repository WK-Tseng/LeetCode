class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for i in range(n)]
        ans = 0

        for i, (x0, y0, r0) in enumerate(bombs):
            for j, (x1, y1, _) in enumerate(bombs):
                if i != j and (x1-x0)**2 + (y1-y0)**2 <= r0**2:
                    g[i] += [j]

        def dfs(node, visited):
            for child in g[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))

        return ans