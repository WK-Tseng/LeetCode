class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        mod = 10**9 + 7
        result = [1] + [0] * n
        for i in range(len(words[0])):
            count = Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                result[j + 1] += result[j] * count[target[j]] % mod
        return result[n] % mod