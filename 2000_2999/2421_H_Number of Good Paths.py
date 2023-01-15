class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        node_map = {i:set() for i in range(len(vals))}

        for node_1, node_2 in edges:
            node_map[node_1].add(node_2)
            node_map[node_2].add(node_1)


        vals_idx_dict = collections.defaultdict(list) 
        for i, v in enumerate(vals):
            vals_idx_dict[v].append(i)

        result = len(vals)
        groups = []
        for val in sorted(vals_idx_dict.keys()):
            for idx in vals_idx_dict[val]:
                
                add_group_idx = []

                for i, group in enumerate(groups):
                    if idx in group['connect']:
                        add_group_idx.insert(0, i)

                        if group['current_val'] == val:
                            group['val_count'] += 1
                        else:
                            group['val_count'] = 1
                            group['current_val'] = val
                
                groups.append(
                    {
                        'val_count' : 1,
                        'connect': set(list(node_map[idx])),
                        'current_val': val
                    }
                )
                add_group_idx.insert(0, len(groups)-1)
                
                for i in range(1, len(add_group_idx)):
                    group_1 = groups[add_group_idx[i-1]]
                    group_2 = groups[add_group_idx[i]]

                    group_2['val_count'] += (group_1['val_count'] - 1)
                    group_2['connect'] |= group_1['connect']

                    groups.pop(add_group_idx[i-1])

            for group in groups:
                if group['current_val'] == val:
                    count = group['val_count']
                    add = (count * (count - 1)) // 2
                    result += add
                
        return result