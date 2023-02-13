class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set((int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])) for deadend in deadends)
        target_tuple = (int(target[0]), int(target[1]), int(target[2]), int(target[3]))
        visit = deadends_set
        queue = set([(0,0,0,0)])
        count = 0

        if (0,0,0,0) in visit:
            return -1

        while queue:
            visit |= queue
            next_queue = set()
            for slots in queue:

                if slots == target_tuple:
                    return count

                slots = list(slots)
                for i in range(4):
                    temp = slots[i]

                    slots[i] += 1
                    if slots[i] == 10:
                        slots[i] =  0

                    next_slots = tuple(slots)
                    if next_slots not in visit:
                        next_queue.add(next_slots)

                    slots[i] = temp
                    slots[i] -= 1
                    if slots[i] == -1:
                        slots[i] =  9
                    
                    next_slots = tuple(slots)
                    if next_slots not in visit:
                        next_queue.add(next_slots)
                    
                    slots[i] = temp
            
            queue = next_queue
            count += 1

            # print(queue)

        return -1