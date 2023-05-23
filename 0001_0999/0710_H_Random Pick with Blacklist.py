class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blackSet = set(blacklist)
        self.nn = n - len(self.blackSet)

        key = [i for i in self.blackSet if i < self.nn]
        val = [i for i in range(self.nn, self.n) if i not in self.blackSet]
        self.dataDict = dict(zip(key, val))

    def pick(self) -> int:
        i = random.randint(0, self.nn-1)
        return self.dataDict.get(i, i)
        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()