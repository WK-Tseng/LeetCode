class Solution:
    # AC, fast
    def removeStones(self, stones: List[List[int]]) -> int:
        def DFS(stones_set, point):
            stones_set.discard(point)
            x, y = point
            for p in row_dict[x]:
                if p in stones_set:
                    DFS(stones_set, p)
            
            for p in column_dict[y]:
                if p in stones_set:
                    DFS(stones_set, p)

        stones_set = set()
        row_dict = collections.defaultdict(set)
        column_dict = collections.defaultdict(set)
        for x, y in stones:
            point = (x, y)
            stones_set.add(point)
            row_dict[x].add(point)
            column_dict[y].add(point)

        count = 0
        for x, y in stones:
            point = (x, y)
            if point in stones_set:
                DFS(stones_set, point)
                count += 1
        
        return len(stones) - count

    # AC
    # def removeStones(self, stones: List[List[int]]) -> int:
    #     island = []
    #     for stone in stones:
    #         x, y = stone

    #         idx_list = []
    #         for idx, data in enumerate(island):
    #             if x in data[0] or y in data[1]:
    #                 idx_list.append(idx)

    #         if len(idx_list) > 0:
    #             x_set = set([x])
    #             y_set = set([y])

    #             for idx in idx_list[::-1]:
    #                 x_set |= island[idx][0]
    #                 y_set |= island[idx][1]

    #                 island.pop(idx)
                
    #             island.append([x_set, y_set])
    #         else:
    #             island.append([set([x]), set([y])])
        
    #     return len(stones) - len(island)