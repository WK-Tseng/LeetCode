class Solution:
    def frequencySort(self, s: str) -> str:
        sDict = {}
        for c in s:
            sDict[c] = sDict.get(c, 0) + 1

        tDict = {}
        for c in sDict:
            times = sDict[c]
            data = tDict.get(times, [])
            data.append(c)
            tDict[times] = data

        result = []
        for times in sorted(list(tDict.keys()), reverse=True):
            result += [c*times for c in tDict[times]] 

        return ''.join(result)