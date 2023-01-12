class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        edge_dict = collections.defaultdict(set)
        for p1, p2 in edges:
            edge_dict[p1].add(p2)
            edge_dict[p2].add(p1)
        
        visit = set()
        queue = [0]
        while queue:
            next_queue = []
            for start in queue:
                visit.add(start)
                remove_p = set()
                for p in edge_dict[start]:
                    if p in visit:
                        remove_p.add(p)
                    else:
                        next_queue.append(p)
                edge_dict[start] -= remove_p
                
            queue = None
            if len(next_queue) > 0:
                queue = next_queue

        # print(visit)
        # print(edge_dict)
        
        result = [0] * n

        def DFS(start):

            this_result = Counter()
            
            for p in edge_dict[start]:
                this_result += DFS(p)
            
            label = labels[start]
            this_result += Counter([label])
            result[start] = this_result[label]
            return this_result

        DFS(0)
        return result