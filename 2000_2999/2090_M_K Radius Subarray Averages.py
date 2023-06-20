class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        stack = []
        result = []
        total = 0
        count = 0
        target = 1 + 2 * k

        for num in nums:
            stack.append(num)
            total += num
            count += 1

            if count == target:
                result.append(total // target)

            elif count > target:
                count -= 1
                total -= stack.pop(0)
                result.append(total // target)

            else:
                result.append(-1)

        for _ in range(k):
            result.pop(0)
            result.append(-1)

        # print(result)
        # print(stack)

        return result