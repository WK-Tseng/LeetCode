class Solution:
    # AC
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        arrLen = len(arr)
        dp = {}

        for num in arr:
            lastNum = num - difference
            if lastNum in dp:
                dp[num] = dp[lastNum] + 1
            else:
                dp[num] = 1

        return max(dp.values())

    # timeout
    # def longestSubsequence(self, arr: List[int], difference: int) -> int:
    #     arrLen = len(arr)
    #     arrDict = collections.defaultdict(set)

    #     for i in range(arrLen):
    #         arrDict[arr[i]].add(i)

    #     # print(arrDict)

    #     result = 1

    #     for i in range(arrLen):
    #         # print('---------', i)

    #         count = 1
    #         idx = i
    #         num = arr[idx]
    #         nextNum = num + difference
    #         arrDict[num].discard(idx)

    #         temp = set(filter(lambda x:x>idx, arrDict[nextNum]))
    #         nextMinIdx = min(temp) if temp else None

    #         while nextMinIdx:
    #             num = nextNum
    #             nextNum = num + difference
    #             arrDict[num].discard(idx)

    #             idx = nextMinIdx
    #             temp = set(filter(lambda x:x>idx, arrDict[nextNum]))
    #             nextMinIdx = min(temp) if temp else None

    #             count += 1

    #             # print('=== ', idx, nextMinIdx)
            
    #         result = max(result, count)
    #         if i + result >= arrLen:
    #             break

    #         # print(i, count)

    #     return result