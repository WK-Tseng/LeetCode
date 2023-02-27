class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        result = len(counter)

        for c in sorted(counter.values()):
            k -= c
            if k < 0:
                break
            result -= 1

        return result

    # AC, slow
    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    #     counter = Counter(arr)
    #     arr.sort(key=lambda x : (counter[x], x))
    #     return len(set(arr[k:]))