class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        one2first = arr[0] - 1
        first2last = arr[-1] - arr[0] - len(arr) + 1

        if k <= one2first:
            return k
        
        k -= one2first
        idx = 0
        for num in range(arr[0], arr[-1]):
            if arr[idx] == num:
                idx += 1
            else:
                k -= 1
                if k == 0:
                    return num

        return arr[-1] + k