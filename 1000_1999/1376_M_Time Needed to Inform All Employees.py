class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_dict = collections.defaultdict(list)
        for i, m in enumerate(manager):
            manager_dict[m].append(i)

        def DFS(headID):
            time = 0
            for m in manager_dict[headID]:
                time = max(time, informTime[m] + DFS(m))
            return time

        # def DFS(headID):
        #     return max([(informTime[m] + DFS(m)) for m in manager_dict[headID]] or [0])

        return DFS(-1)