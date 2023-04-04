class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people = people[::-1]
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: 
                j -= 1
            i += 1
        return i