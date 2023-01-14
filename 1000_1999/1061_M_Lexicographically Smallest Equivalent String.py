class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        c_idx_dict = {}
        c_set_list = []
        # i = 0

        for c1, c2 in zip(s1, s2):
            idx1, idx2 = c_idx_dict.get(c1, -1), c_idx_dict.get(c2, -1)

            if idx1 == -1 and idx2 == -1:
                c_set_list.append(set([c1, c2]))
                idx = len(c_set_list) - 1
                c_idx_dict[c1] = idx
                c_idx_dict[c2] = idx
            elif (idx1 != -1 and idx2 == -1) or (idx1 == -1 and idx2 != -1):
                idx = max(idx1, idx2)

                c_set_list[idx].add(c1)
                c_set_list[idx].add(c2)

                c_idx_dict[c1] = idx
                c_idx_dict[c2] = idx
            elif idx1 == idx2:
                pass
            else:
                set1 = c_set_list[idx1]
                set2 = c_set_list[idx2]
                set1 |= set2

                for c in set2:
                    c_idx_dict[c] = idx1
                set2.clear()
                set2.add('.')
            
            # print('+++++++++++++++++++++++++++')
            # for s in c_set_list:
            #     print(i, id(s), s)
            # i += 1

        # print('---------------------------------')
        # print(c_idx_dict)
        # print(c_set_list)
        # for s in c_set_list:
        #     print(id(s), s)

        c_set_list = [min(s) for s in c_set_list]

        # print(c_set_list)

        return ''.join([c_set_list[c_idx_dict[c]] if c in c_idx_dict else c for c in baseStr])
