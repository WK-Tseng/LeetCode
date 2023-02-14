class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        if n == 1:
            return True
        
        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                queue = [i]
                while queue:
                    p = queue.pop(0)
                    
                    this_color = color[p]
                    next_color = this_color * -1
                    for next_p in graph[p]:
                        if color[next_p] == 0:
                            color[next_p] = next_color
                            queue.append(next_p)
                        # elif color[next_p] == next_color:
                        #     pass
                        elif color[next_p] != next_color:
                            return False
            # print(i, color)

        return True