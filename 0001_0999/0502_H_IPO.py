class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = sorted(zip(capital, profits), key=lambda x : x[0])
        project_len = len(project)
        
        heap = []
        heap_count = 0
        for _ in range(k):
            while heap_count < project_len and project[heap_count][0] <= w:
                heapq.heappush(heap, -project[heap_count][1])
                heap_count += 1
            if heap:
                w -= heapq.heappop(heap)
        
        return w

    # timeout
    # def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    #     profits_dict = collections.defaultdict(list)
    #     for prfit, cap in zip(profits, capital):
    #         heapq.heappush(profits_dict[cap], -prfit)

    #     cap_keys = list(profits_dict.keys())
    #     cap_keys.sort()

    #     while k > 0:
    #         k -= 1

    #         profit_cap = []
    #         for cap in cap_keys:
    #             if cap <= w:
    #                 heapq.heappush(profit_cap, (profits_dict[cap][0], cap))
    #             else:
    #                 break

    #         if len(profit_cap) == 0:
    #             break

    #         max_profit, cap = profit_cap[0]
    #         w += -max_profit

    #         heapq.heappop(profits_dict[cap])
    #         if len(profits_dict[cap]) == 0:
    #             cap_keys.remove(cap)

    #     return w