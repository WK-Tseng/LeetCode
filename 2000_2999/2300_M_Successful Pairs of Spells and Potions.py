class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        temp_spells = [(i, s) for i, s in enumerate(spells)]
        temp_spells.sort(key=lambda x : x[1])
        spells = [s for _, s in temp_spells]
        
        # spells.sort()
        potions.sort()

        potions_len = len(potions)
        result = []

        start = -1
        for s in spells:
            if s * potions[-1] >= success:
                for i in range(potions_len):
                    if s * potions[i] >= success:
                        start = i
                        result.append(potions_len - i)
                        break
                break
            else:
                result.append(0)
        
        result_len = len(result)
        for s in spells[result_len:]:
            flag = False
            for i in range(start, -1, -1):
                if s * potions[i] < success:
                    start = i + 1
                    flag = True
                    break
            if flag:
                result.append(potions_len - start)
            else:
                result.append(potions_len)
        
        temp_result = [(temp_spells[i], result[i]) for i in range(len(result))]
        temp_result.sort(key=lambda x : x[0])
        result = [r for _, r in temp_result]

        return result
                