class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set([0])
        keys = set(rooms[0])

        while len(keys) > 0:
            newKeys = set()
            for key in keys:
                if key not in visit:
                    visit.add(key)
                    for newKey in rooms[key]:
                        newKeys.add(newKey)
            keys = newKeys
        
        return len(visit) == len(rooms) 