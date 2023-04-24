class Solution:
    def countVowels(self, word: str) -> int:
        wordLen = len(word)
        count = wordLen
        diff = wordLen
        result = 0
        for w in word:
            # result += (w in 'aeiou') * count
            if w in 'aeiou':
                result += count
            diff -= 2
            count += diff

        return result

    # AC, slow
    # def countVowels(self, word: str) -> int:
    #     flag = ['a', 'e', 'i', 'o', 'u']
    #     wordList = [w in flag for w in word]
    #     wordLen = len(word)

    #     wordCount = [0] * wordLen
    #     diff = wordLen - 2
    #     wordCount[0] = wordLen
    #     for i in range(1, wordLen):
    #         wordCount[i] = wordCount[i-1] + diff
    #         diff -= 2

    #     return sum(flag*count for flag, count in zip(wordList, wordCount))