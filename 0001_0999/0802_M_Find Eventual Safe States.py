class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = set(i for i, g in enumerate(graph) if len(g) == 0)
        # print(terminal)

        if len(terminal) == 0:
            return []

        n = len(graph)
        graph = [set(g) for g  in graph]
        exit_flag = False
        while not exit_flag:
            exit_flag = True
            for i, g in enumerate(graph):
                if len(g) > 0: 
                    g -= terminal
                    if len(g) == 0:
                        terminal.add(i)
                        exit_flag = False

            # print(terminal)
            # print(graph)

        return sorted(list(terminal))