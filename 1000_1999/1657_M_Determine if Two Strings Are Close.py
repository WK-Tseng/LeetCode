class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if not len(word1) == len(word2):
            return False
        
        set1, set2 = set(word1), set(word2)
        if set1 != set2:
            return False

        dict1, dict2 = {}, {}

        for i in range(len(word1)):
            dict1[word1[i]] = dict1.get(word1[i], 0) + 1
            dict2[word2[i]] = dict2.get(word2[i], 0) + 1

        # print(dict1)
        # print(dict2)

        if len(dict1) != len(dict2):
            return False

        timesDict = {}
        for v in dict1.values():
            timesDict[v] = timesDict.get(v, 0) + 1

        # print(timesDict)

        for v in dict2.values():
            timesDict[v] = timesDict.get(v, 0) - 1
            if timesDict[v] == 0:
                del timesDict[v]

        # print(timesDict)

        if len(timesDict) != 0:
            return False

        return True

        