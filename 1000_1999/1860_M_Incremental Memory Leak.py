class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        count = 1
        while memory1 >= count or memory2 >= count:
            if memory1 >= memory2:
                memory1 -= count
            else:
                memory2 -= count
            count += 1
            
        return [count, memory1, memory2]