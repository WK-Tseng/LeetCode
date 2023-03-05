class Solution:
    def minJumps(self, arr: List[int]) -> int:
        jump_same = collections.defaultdict(set)
        for i, n in enumerate(arr):
            jump_same[n].add(i)

        queue = set()
        visit = set()
        visit_same = set()

        queue.add(0)
        end = len(arr) - 1

        count = 0

        while queue:
            next_queue = set()
            visit |= queue

            for p in queue:
                if p == end:
                    return count
                
                for np in [p+1, p-1]:
                    if 0 <= np <= end and np not in visit:
                        next_queue.add(np)

                if arr[p] not in visit_same:
                    for np in jump_same[arr[p]]:
                        if np not in visit:
                            next_queue.add(np)
                    visit_same.add(arr[p])

            queue = next_queue
            count += 1
        
        return -1

    # AC, slow
    # def minJumps(self, arr: List[int]) -> int:
    #     jump_same = collections.defaultdict(set)
    #     for i, n in enumerate(arr):
    #         jump_same[n].add(i)

    #     queue = []
    #     visit = set()
    #     visit_same = set()

    #     queue.append((0, 0)) # count, idx
    #     end = len(arr) - 1

    #     while queue:
    #         count, idx = queue.pop(0)
    #         # print(count, idx, arr[idx], queue)
            
    #         if idx == end:
    #             return count
            
    #         for np in [idx+1, idx-1]:
    #             if 0 <= np <= end and np not in visit:
    #                 visit.add(np)
    #                 queue.append((count+1, np))

    #         if arr[idx] not in visit_same:
    #             for np in jump_same[arr[idx]]:
    #                 if np not in visit:
    #                     queue.append((count+1, np))
    #                     visit.add(np)
    #             visit_same.add(arr[idx])
        
    #     return -1