class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sLen = len(s)
        wordsLen = len(words)
        wordLen = len(words[0])
        allAppearWord = [0] * sLen
        
        wordCount = {}
        for word in words:
            wordCount[word] = wordCount.get(word, 0) + 1

        def DFS(startIdx, remainingWordsCount):
            if remainingWordsCount == 0:
                return True

            if startIdx > sLen:
                return False

            thisWord = s[startIdx : startIdx + wordLen]
            if thisWord in wordCount and wordCount[thisWord] > 0:
                wordCount[thisWord] -= 1
                _result = DFS(startIdx + wordLen, remainingWordsCount - 1)
                wordCount[thisWord] += 1
                return _result

            return False

        result = []
        for i in range(sLen - wordLen * wordsLen + 1):
            if DFS(i, wordsLen):
                result.append(i)

        return result