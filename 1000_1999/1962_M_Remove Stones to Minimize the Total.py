import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_counter = Counter(piles)
        key_list = list(piles_counter.keys())
        key_list.sort(reverse=True)

        for _ in range(k):
            # key = max(piles_counter.keys())
            key = key_list[0]
            counter = piles_counter[key]
            counter -= 1
            if counter > 0:
                piles_counter[key] = counter
            else:
                key_list.pop(0)
                piles_counter.pop(key)
            
            result = key - math.floor(key / 2.0)
            if result not in piles_counter:
                flag = False
                for i in range(len(key_list)):
                    if result > key_list[i]:
                        key_list.insert(i, result)
                        flag = True
                        break
                if not flag:
                    key_list.append(result)
            piles_counter[result] = piles_counter.get(result, 0) + 1
            # print(key_list)
            # print(piles_counter)

        reslut = 0
        for key, val in piles_counter.items():
            reslut += key * val

        return reslut