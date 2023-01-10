class Trie:

    def __init__(self):
        # self.root = collections.defaultdict(dict)
        self.root = [False, {}]

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            next_temp = None
            if c in temp[1]:
                next_temp = temp[1][c]
            else:
                next_temp = [False, {}]
                temp[1][c] = next_temp
            temp = next_temp
        temp[0] = True

    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c in temp[1]:
                temp = temp[1][c]
            else:
                return False

        return temp[0]

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c in temp[1]:
                temp = temp[1][c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)