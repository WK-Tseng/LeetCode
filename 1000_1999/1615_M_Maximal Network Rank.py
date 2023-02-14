class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roads_dict = collections.defaultdict(set)
        for c1, c2 in roads:
            roads_dict[c1].add(c2)
            roads_dict[c2].add(c1)
        
        roads_key_dict = collections.defaultdict(set)
        for key in roads_dict:
            l = len(roads_dict[key])
            roads_key_dict[l].add(key)

        # print(roads_key_dict)

        connect_rank = list(roads_key_dict.keys())
        connect_rank.sort(key=lambda x: -x)

        # print(connect_rank)

        result = 0

        if len(connect_rank) == 0:
            pass
        elif len(roads_key_dict[connect_rank[0]]) > 1:
            node_set = roads_key_dict[connect_rank[0]]
            overlay = True
            for n1 in node_set:
                for n2 in node_set:
                    if n1 != n2:
                        if n2 not in roads_dict[n1]:
                            overlay = False
                            break
                if not overlay:
                    break

            result = connect_rank[0] * 2
            if overlay:
                result -= 1
        else:
            node_set_0 = roads_key_dict[connect_rank[0]]
            node_set_1 = roads_key_dict[connect_rank[1]]
            overlay = True
            for n1 in node_set_0:
                for n2 in node_set_1:
                    if n1 != n2:
                        if n2 not in roads_dict[n1]:
                            overlay = False
                            break
                if not overlay:
                    break
            
            result = connect_rank[0] + connect_rank[1]
            if overlay:
                result -= 1

        return result