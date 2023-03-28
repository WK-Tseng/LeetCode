class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        cost = 0
        day7, day30 = [], []
        
        for d in days:
            while len(day7) > 0 and day7[0][0] + 7 <= d:
                day7.pop(0)
            while len(day30) > 0 and day30[0][0] + 30 <= d:
                day30.pop(0)

            day7.append((d, cost + costs[1]))
            day30.append((d, cost + costs[2]))
            
            cost = min(cost + costs[0], day7[0][1], day30[0][1])

        return cost
