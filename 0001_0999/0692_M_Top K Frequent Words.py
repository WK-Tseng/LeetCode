class Solution:
    # AC, fast
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsDict = Counter(words)
        wordsList = [(word, -times) for word, times in wordsDict.items()]
        wordsList.sort(key=lambda x: (x[1], x[0]))

        return [wordsList[i][0] for i in range(k)]


    # AC, slow
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     wordsDict = Counter(words)
    #     timesDict = {}
    #     for word, times in wordsDict.items():
    #         timesDict[times] = timesDict.get(times, []) + [word]

    #     result = []
    #     while k > 0:
    #         times = max(timesDict.keys())
    #         wordsList = timesDict.pop(times)
    #         wordsList.sort()
    #         result += wordsList[:min(k, len(wordsList))]
    #         k -= len(wordsList)
            
    #     return result

