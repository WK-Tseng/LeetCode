class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visit = set()
        for f in forbidden:
            # point, last_direct
            visit.add((f, 1))
            visit.add((f, -1))

        queue = [(0, 0, 0)] # point, count, last_direct
        while queue:
            p, c, d = queue.pop(0)

            if p == x:
                return c
            
            if (p+a, 1) not in visit and p + a <= 6000:
                queue.append((p+a, c+1, 1))
                visit.add((p+a, 1))
            
            if d != -1 and (p-b, -1) not in visit and p - b >= 0:
                queue.append((p-b, c+1, -1))
                visit.add((p-b, -1))
            # print(p, queue)

        return -1