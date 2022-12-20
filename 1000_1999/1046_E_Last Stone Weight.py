class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        while len(stones) > 1:
            stone1 = stones.pop(-1)
            stone2 = stones.pop(-1)
            if stone1 != stone2:
                newStone = stone1 - stone2

                if len(stones) == 0:
                    stones.insert(0, newStone)
                elif newStone <= stones[0]:
                    stones.insert(0, newStone)
                else:
                    # it can change to binary search.
                    for i in range(len(stones)-1, -1, -1):
                        if stones[i] < newStone:
                            stones.insert(i+1, newStone)
                            break

        return stones[0] if len(stones) != 0 else 0