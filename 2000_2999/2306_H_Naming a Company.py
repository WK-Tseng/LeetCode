class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideas_dict = collections.defaultdict(set)
        for idea in ideas:
            ideas_dict[idea[0]].add(idea[1:])

        # print(ideas_dict)
        key_list = list(ideas_dict.keys())
        key_list_len = len(key_list)
        count = 0
        for i in range(key_list_len):
            id_1 = ideas_dict[key_list[i]]
            id_1_len = len(id_1)
            for j in range(i+1, key_list_len):
                id_2 = ideas_dict[key_list[j]]
                id_12 = id_1 & id_2
                id_12_len = len(id_12)
                # d1, d2 = id_1 - id_12, id_2 - id_12
                # count += len(d1) * len(d2)
                count += (id_1_len - id_12_len) * (len(id_2) - id_12_len)

        return count*2

    # def distinctNames(self, ideas: List[str]) -> int:
    #     n = len(ideas)
    #     ideas_set = set(ideas)
    #     count = 0
    #     for i in range(n):
    #         n1 = ideas[i]
    #         for j in range(i+1, n):
    #             n2 = ideas[j]
    #             if (n1[0]+n2[1:]) in ideas_set or (n2[0]+n1[1:]) in ideas_set:
    #                 pass
    #             else:
    #                 count += 2

    #     return count