class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [(cap - rock) for cap, rock in zip(capacity, rocks)]
        diff.sort()

        result = 0
        needTotal = 0
        for need in diff:
            needTotal += need
            if needTotal <= additionalRocks:
                result += 1
            else:
                break

        return result