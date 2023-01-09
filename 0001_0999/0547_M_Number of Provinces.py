class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        isConnected_dict = {}
        for i, isConnected_list in enumerate(isConnected):
            isConnected_dict[i] = [idx for idx, v in enumerate(isConnected_list) if v == 1]
        # print(isConnected_dict)

        def DFS(cities, i):
            cities.discard(i)

            for connect in isConnected_dict[i]:
                if connect in cities:
                    DFS(cities, connect)
        
        cities = set(i for i in range(len(isConnected)))
        # print(cities)

        count = 0
        for i in range(len(isConnected)):
            if i in cities:
                DFS(cities, i)
                count += 1

        return count