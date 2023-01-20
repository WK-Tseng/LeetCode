class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        result = [False] * s_len

        for word in wordDict:
            word_len = len(word)
            end = 0 + word_len
            if end-1 < s_len and not result[end-1] and s[0:end] == word:
                result[0+word_len-1] = True
        # print(result)

        for i in range(1, s_len):
            if result[i-1]:
                for word in wordDict:
                    word_len = len(word)
                    end = i + word_len
                    if end-1 < s_len and not result[end-1] and s[i:end] == word:
                        result[i+word_len-1] = True

        # print(result)

        return result[-1]
                