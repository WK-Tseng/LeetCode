class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senatorQueue = [[], []]
        for i, s in enumerate(senate):
            if s == 'R':
                senatorQueue[0].append(i)
            else:
                senatorQueue[1].append(i)

        while len(senatorQueue[0]) > 0 and len(senatorQueue[1]) > 0:
            a, b = senatorQueue[0].pop(0), senatorQueue[1].pop(0)
            if a < b:
                senatorQueue[0].append(a+n)
            else:
                senatorQueue[1].append(b+n)

        # print(len(senatorQueue[0]), len(senatorQueue[1]))

        return "Radiant" if len(senatorQueue[0]) > len(senatorQueue[1]) else "Dire"