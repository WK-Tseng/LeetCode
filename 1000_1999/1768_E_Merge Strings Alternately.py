class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        nn = min(len(word1), len(word2))
        return ''.join(c1+c2 for c1, c2 in zip(word1[:nn], word2[:nn])) + word1[nn:] + word2[nn:]
