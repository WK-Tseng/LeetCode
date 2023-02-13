class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_set.add(beginWord)
        word_set.add(endWord)
        
        n = len(beginWord)
        word_dict = collections.defaultdict(set)
        for word in word_set:
            for i in range(n):
                word_idx = word[:i] + '@' + word[i+1:]
                word_dict[word_idx].add(word)

        visit = set()
        queue = set([beginWord])
        count = 1
        while queue:
            visit |= queue
            next_queue = set()
            for word in queue:
                
                if word == endWord:
                    return count

                for i in range(n):
                    word_idx = word[:i] + '@' + word[i+1:]
                    for next_word in word_dict[word_idx]:
                        if next_word not in visit:
                            next_queue.add(next_word)

            queue = next_queue
            count += 1

        return 0