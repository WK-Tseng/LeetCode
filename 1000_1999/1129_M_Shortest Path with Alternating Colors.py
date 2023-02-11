class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        result_flag = float('inf')
        result = [result_flag] * n
        red_dict = collections.defaultdict(set)
        blue_dict = collections.defaultdict(set)

        for a, b in redEdges:
            red_dict[a].add(b)

        for a, b in blueEdges:
            blue_dict[a].add(b)

        visit_red = set()
        visit_blue = set()
        queue = set([0])
        count = 0
        color = True # red
        while queue:
            next_dict, next_visit, next_queue = None, None, set()
            if color:
                visit_blue |= queue
                next_dict = red_dict
                next_visit = visit_red
            else:
                visit_red |= queue
                next_dict = blue_dict
                next_visit = visit_blue

            for p in queue:
                result[p] = min(result[p], count)
                next_queue |= (next_dict[p] - next_visit)
            queue = next_queue
            count += 1
            color = not color

        visit_red.clear()
        visit_blue.clear()
        queue.clear()
        queue.add(0)
        count = 0
        color = False # blue
        while queue:
            next_dict, next_visit, next_queue = None, None, set()
            if color:
                visit_blue |= queue
                next_dict = red_dict
                next_visit = visit_red
            else:
                visit_red |= queue
                next_dict = blue_dict
                next_visit = visit_blue

            for p in queue:
                result[p] = min(result[p], count)
                next_queue |= (next_dict[p] - next_visit)

            queue = next_queue
            count += 1
            color = not color
        
        result = [-1 if r == result_flag else r for r in result]
        return result