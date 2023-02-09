class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # conn_dict = collections.defaultdict(set)
        conn_dict = {i:set() for i in range(n)}
        node_set = set(i for i in range(n))
        count = 0

        for n1, n2 in connections:
            conn_dict[n1].add(n2)
            conn_dict[n2].add(n1)

            if n1 in node_set or n2 in node_set:
                node_set.discard(n1)
                node_set.discard(n2)
            else:
                count += 1

        # print(conn_dict)

        visit = set()
        group_count = 0
        for start in conn_dict:
            if start not in visit:
                group_count += 1
                queue = set()
                queue.add(start)
                while queue:
                    visit |= queue
                    next_queue = set()
                    for p in queue:
                        # for next_p in conn_dict[p]:
                        #     if next_p not in visit:
                        #         next_queue.add(next_p)
                        next_queue |= (conn_dict[p] - visit)
                    queue = None
                    if len(next_queue) > 0:
                        queue = next_queue
        # print(visit)
        # print(group_count)
        # print(count)
        
        if count+1 >= group_count:
            return group_count-1
        return -1

    # def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    #     node_set = set(i for i in range(n))
    #     # print(node_set)

    #     count = 0
    #     for n1, n2 in connections:
    #         if n1 in node_set or n2 in node_set:
    #             node_set.discard(n1)
    #             node_set.discard(n2)
    #         else:
    #             count += 1

    #     # print(node_set)
    #     # print(count)
    #     return len(node_set) if count >= len(node_set) else -1