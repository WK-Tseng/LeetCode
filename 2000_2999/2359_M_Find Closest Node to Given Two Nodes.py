class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        max_flag = N *10
        dist = [[max_flag] * N for _ in range(2)]

        def DFS(group, now_dist, node):

            dist[group][node] = now_dist

            next_node = edges[node]
            if next_node != -1 and dist[group][next_node] == max_flag:
                DFS(group, now_dist+1, next_node)

        DFS(0, 0, node1)
        DFS(1, 0, node2)

        # print(dist[0])
        # print(dist[1])

        totoal_dist = [max(d1, d2) for d1, d2 in zip(dist[0], dist[1])]
        min_dist = min(totoal_dist)
        result = totoal_dist.index(min_dist)
        # print(totoal_dist)
        # print(min_dist)
        # print(result)

        return -1 if min_dist == max_flag else result

    # timeout, BFS
    # def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

    #     visit1 = set()
    #     queue1 = set([node1])

    #     visit2 = set()
    #     queue2 = set([node2])

    #     while queue1 or queue2:

    #         if queue1:
    #             visit1 |= queue1
    #             next_queue1 = set()
    #             for p in queue1:
    #                 next_p = edges[p]
    #                 if next_p != -1 and next_p not in visit1:
    #                     next_queue1.add(next_p)
                
    #             queue1 = None
    #             if len(next_queue1) > 0:
    #                 queue1 = next_queue1

    #         if queue2:
    #             visit2 |= queue2
    #             next_queue2 = set()
    #             for p in queue2:
    #                 next_p = edges[p]
    #                 if next_p != -1 and next_p not in visit2:
    #                     next_queue2.add(next_p)
                
    #             queue2 = None
    #             if len(next_queue2) > 0:
    #                 queue2 = next_queue2

    #         visit = visit1 & visit2
    #         if len(visit) > 0:
    #             return list(visit)[0] 

    #     return -1
            