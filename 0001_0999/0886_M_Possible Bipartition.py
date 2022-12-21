class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikesDict = {i: set() for i in range(1, n + 1)}
        for a, b in dislikes:
            dislikesDict[a].add(b)
            dislikesDict[b].add(a)

        groupsState = [0] * (n+1)

        def setGroup(people, state):
            groupsState[people] = state

            for dislike_people in dislikesDict[people]:
                if groupsState[dislike_people] == state:
                    return False
                if groupsState[dislike_people] == 0:
                    if not setGroup(dislike_people, -state):
                        return False
            
            return True

        for people in range(1, n+1):
            if groupsState[people] == 0:
                if not setGroup(people, 1):
                    return False

        return True
        

    # timeout
    # def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    #     dislikesDict = {i: set() for i in range(1, n + 1)}
    #     for a, b in dislikes:
    #         dislikesDict[a].add(b)
    #         dislikesDict[b].add(a)

    #     # print(dislikesDict)
    #     # print(likesDict)

    #     groups = [set(), set()]
    #     dislikeGroups = [set(), set()]

    #     def DFS(people):
    #         if people == n + 1:
    #             return len(groups[0]) + len(groups[1]) == n
            
    #         for i in range(min(2, people)):
    #             if people not in dislikeGroups[i]:
    #                 groups[i].add(people)
    #                 diffSet = dislikesDict[people] - dislikeGroups[i]
    #                 dislikeGroups[i] |= diffSet
    #                 flag = DFS(people+1)
    #                 dislikeGroups[i] -= diffSet
    #                 groups[i].remove(people)
                    
    #                 if flag:
    #                     return True

    #         return False

    #     return DFS(1)