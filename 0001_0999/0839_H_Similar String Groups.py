class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strCountList = [set([c+str(i) for i,c in enumerate(s)]) for s in strs]

        results = [[strCountList[0]]]
        for data in strCountList[1:]:
            find = False
            for result in results:
                flag = False
                for d in result:
                    if len(d - data) <= 2:
                        flag = True
                        break
                if flag:
                    result.append(data)
                    find = True
                    break
            
            if not find:
                results.append([data])

        # print(results)
        flag = False

        while True:
            flag = False
            for i in range(len(results)):
                for j in range(i+1, len(results)):
                    
                    for d1 in results[i]:
                        for d2 in results[j]:
                            if len(d1-d2) <= 2:
                                flag = True
                                break
                        if flag:
                            break
                    
                    if flag:
                        results[i] += results[j]
                        del results[j]
                        break
                if flag:
                    break

            if not flag:
                break


        return len(results)