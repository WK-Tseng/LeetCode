class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []

        candidatesDict = Counter(candidates)

        def DFS(keyList, t):
            if t < 0:
                return 
            elif t == 0:
                result.append([n for n in temp])
                return 

            for i, n in enumerate(keyList):
                for times in range(1, candidatesDict[n]+1):
                    temp.append((n, times))
                    DFS(keyList[i+1:], t - n*times)
                    temp[:] = temp[:-1]
        
        keyList = sorted(candidatesDict.keys())
        DFS(keyList, target)

        finish = []
        for temp in result:
            this = []
            for n, t in temp:
                this += [n] * t
            finish.append(this)

        return finish
       
        

        # 30
        # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        # 27
        # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]