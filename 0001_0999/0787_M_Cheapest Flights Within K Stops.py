class Solution:
    # 最短路徑演算法: Dijkstra 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flights_dict = collections.defaultdict(dict)
        for _from, _to, _price in flights:
            flights_dict[_from][_to] = _price

        # price, node, step
        queue = [(0, src, k+1)]
        visit = [0] * n

        while queue:
            # get min price
            price, node, step = heapq.heappop(queue)
            # print(price, node, step)
            # print(visit)
            
            if node == dst:
                return price
            
            if visit[node] < step:
                visit[node] = step
                for to, add_price in flights_dict[node].items():
                    heapq.heappush(queue, (price+add_price, to, step-1))

        return -1

    # DFS, timeout
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

    #     flights_dict = {i:[] for i in range(n)}
    #     for _from, _to, _price in flights:
    #         flights_dict[_from].append((_to, _price))

    #     max_price = [float('inf')]
    #     max_step = k + 2

    #     def DFS(src, visit, step, now_price):
    #         visit.add(src)

    #         if step > max_step or now_price > max_price[0]:
    #             pass
    #         elif src == dst:
    #             max_price[0] = min(max_price[0], now_price)
    #         else:
    #             for to, price in flights_dict[src]:
    #                 if to not in visit:
    #                     DFS(to, visit, step + 1, now_price + price)

    #         visit.remove(src)

    #     DFS(src, set(), 1, 0)

    #     return -1 if max_price[0] == float('inf') else max_price[0]