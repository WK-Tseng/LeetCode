class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        visit = set()
        queue = [(0, 0)]
        while queue:
            a, b = queue.pop(0)
            visit.add((a, b))

            if a + b == targetCapacity:
                return True

            newSet = set()
            newSet.add((jug1Capacity, b))
            newSet.add((a, jug2Capacity))
            newSet.add((0, b))
            newSet.add((a, 0))
            newSet.add((min(jug1Capacity, a+b), 0 if jug1Capacity - a > b else b - (jug1Capacity - a)))
            newSet.add((0 if jug2Capacity - b > a else a - (jug2Capacity - b), min(jug2Capacity, a+b)))

            newSet -= visit
            queue += list(newSet)

        return False
            