class Solution:
    # AC, fast
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = Counter(words)
        center = False
        pair = 0

        for word, count in word_dict.items():
            if word[0] == word[1]:
                pair += count
                if count % 2 == 1:
                    center = True
                    pair -= 1

            elif word[0] < word[1]:
                pair_count = word_dict.get(word[::-1], None)
                if pair_count:
                    pair += min(count, pair_count) * 2
        
        if center:
            pair += 1

        return pair * 2

    # AC, slow
    # def longestPalindrome(self, words: List[str]) -> int:
    #     word_dict = {}
    #     pair = 0

    #     for word in words:
    #         if word in word_dict:
    #             pair += 1
    #             word_dict[word] -= 1
    #             if word_dict[word] == 0:
    #                 word_dict.pop(word)
    #         else:
    #             word_dict[word[::-1]] = word_dict.get(word[::-1], 0) + 1

    #     pair *= 4

    #     for word in word_dict:
    #         if word[0] == word[1]:
    #             pair += 2
    #             break

    #     return pair