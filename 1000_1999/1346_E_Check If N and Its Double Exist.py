class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        # print(arr)
        arr_dict = collections.defaultdict(set)
        for i, a in enumerate(arr):
            arr_dict[a].add(i)
        # print(arr_dict)
        for i, a in enumerate(arr):
            aa = a*2
            if aa > arr[-1]:
                break
            if aa in arr_dict:
                if len(arr_dict[aa] - set([i])) > 0:
                    return True
        return False