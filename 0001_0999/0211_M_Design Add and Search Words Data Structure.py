class WordDictionary:

    def __init__(self):
        self.data = {}

    def addWord(self, word: str) -> None:
        _data = self.data
        for c in word:
            if c in _data:
                _data = _data[c]
            else:
                _data[c] = {}
                _data = _data[c]
        _data['end'] = True

    def search(self, word: str) -> bool:
        def _search(data, word):
            _data = data
            if len(word) == 0:
                return 'end' in _data
            elif word[0] == '.':
                word = word[1:]
                flag = False
                for i in _data:
                    if i != 'end':
                        flag |= _search(_data[i], word)
                return flag
            elif word[0] in _data:
                return _search(_data[word[0]], word[1:])
            return False
        return  _search(self.data, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)