class SnapshotArray:

    def __init__(self, length: int):
        self.snapData = collections.defaultdict(list)
        self.id = 0

    def set(self, index: int, val: int) -> None:
        if self.snapData[index] and self.snapData[index][-1][0] == self.id:
            self.snapData[index][-1][1] = val
        else:
            self.snapData[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        data = self.snapData[index]
        left, right, resultIdx = 0, len(data) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if data[mid][0] <= snap_id:
                resultIdx = mid
                left = mid + 1
            else:
                right = mid - 1

        if resultIdx == -1:
            return 0
        return data[resultIdx][1]

# Memory Limit Exceeded
# class SnapshotArray:

#     def __init__(self, length: int):
#         self.data = [0] * length
#         self.snapList = []

#     def set(self, index: int, val: int) -> None:
#         self.data[index] = val

#     def snap(self) -> int:
#         self.snapList.append(self.data[:])
#         return len(self.snapList) - 1

#     def get(self, index: int, snap_id: int) -> int:
#         return self.snapList[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)