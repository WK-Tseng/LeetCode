class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len_1, len_2 = len(firstList), len(secondList)
        idx_1, idx_2 = 0, 0

        result = []

        while idx_1 < len_1 and idx_2 < len_2:
            temp = []
            temp.append(max(firstList[idx_1][0], secondList[idx_2][0]))
            temp.append(min(firstList[idx_1][1], secondList[idx_2][1]))

            # print(idx_1, idx_2, temp)

            if temp[0] <= temp[1]:
                result.append(temp)

            if firstList[idx_1][1] > secondList[idx_2][1]:
                idx_2 += 1
            else:
                idx_1 += 1

        return result