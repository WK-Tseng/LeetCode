class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pSet = set(p)
        pLen = len(p)
        spliteIdx = []
        spliteStr = []
        
        start = None
        end = None
        for i in range(len(s)):
            if s[i] in pSet:
                if start is None:
                    start = i
                end = i
            else:
                if start is not None:
                    if end - start + 1 >= pLen:
                        spliteIdx.append(start)
                        spliteStr.append(s[start : end + 1])
                    start = None
                    end = None

        if start is not None:
            if end - start + 1 >= pLen:
                spliteIdx.append(start)
                spliteStr.append(s[start : end + 1])

        if len(spliteIdx) == 0:
            return []

        # AC
        # pDict = Counter(p)
        # pSet = set([item for item in pDict.items()])
        # result = []
        # for idx, subStr in enumerate(spliteStr):
        #     for i in range(0, len(subStr) - pLen+1):
        #         subStrDict = Counter(subStr[i:i+pLen])
        #         subStrSet = set([item for item in subStrDict.items()])

        #         if pSet == subStrSet:
        #             result.append(spliteIdx[idx]+i)
        # return result

        # AC, fast
        result = []
        pDict = Counter(p)
        for idx, subStr in enumerate(spliteStr):
            pDict = Counter(p)
           
            for i in range(pLen - 1):
                pDict[subStr[i]] -= 1

            for i in range(pLen-1, len(subStr)):
                pDict[subStr[i]] -= 1
                if all(v == 0 for v in pDict.values()):
                    result.append(spliteIdx[idx]+i-pLen+1)
                pDict[subStr[i-pLen+1]] += 1

        return result