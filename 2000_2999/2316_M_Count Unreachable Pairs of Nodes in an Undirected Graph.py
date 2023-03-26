class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = collections.defaultdict(set)
        for a, b in edges:
            edges_dict[a].add(b)
            edges_dict[b].add(a)

        visits = set()
        groups = []
        for i in range(n):
            if i not in visits:
                visit = set()
                queue = set([i])
                while queue:
                    visit |= queue
                    next_queue = set()
                    for p in queue:
                        next_queue |= (edges_dict[p] - visit)
                    queue = next_queue

                groups.append(len(visit))
                visits |= visit
        
        groups_len = len(groups)
        groups_pre_sum = [0] * groups_len
        groups_pre_sum[-1] = groups[-1]
        for i in range(groups_len-2, -1, -1):
            groups_pre_sum[i] = groups_pre_sum[i+1] + groups[i]

        result = 0
        for i in range(1, groups_len):
            result += groups[i-1] * groups_pre_sum[i]

        return result