class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.idxDict = defaultdict(list)

        for i, n in enumerate(arr):
            self.idxDict[n].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        
        # 碰運氣，概念就是這區間內越多的數字越容易被抽到
        # for _ in range(max(threshold//100, 10)):
        for _ in range(10):
            k = random.randint(left,right)
            result = self.arr[k]

            low = bisect.bisect_left(self.idxDict[result], left)
            hight = bisect.bisect_right(self.idxDict[result], right)

            if hight - low >= threshold:
                return result
        
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)