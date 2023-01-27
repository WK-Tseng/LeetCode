class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words_set = set(words)

        def DFS(word):

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words_set:
                    if suffix in words_set or DFS(suffix):
                        return True
                        
            return False

        results = []
        for word in words:
            if DFS(word):
                results.append(word)

        return results