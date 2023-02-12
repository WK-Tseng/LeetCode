class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visit = set([start])
        queue = [start]
        while queue:
            p = queue.pop(0)
            step = arr[p]
            
            if step == 0:
                return True

            next_p = p + step
            if next_p < n and next_p not in visit:
                queue.append(next_p)
                visit.add(next_p)
            
            next_p = p - step
            if next_p >= 0 and next_p not in visit:
                queue.append(next_p)
                visit.add(next_p)

        return False