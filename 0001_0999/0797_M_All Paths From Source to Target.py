class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []
        path = []
        def DFS(node):
            path.append(node)

            if node == target:
                result.append(list(path))

            for next_node in graph[node]:
                DFS(next_node)

            path.pop(-1)

        DFS(0)

        return result