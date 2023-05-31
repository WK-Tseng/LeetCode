class UndergroundSystem:

    def __init__(self):
        self.idDict = {}
        self.station = collections.defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idDict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ss, tt = self.idDict[id]
        thisTime = t - tt
        if stationName in self.station[ss]:
            self.station[ss][stationName][0] += thisTime
            self.station[ss][stationName][1] += 1
        else:
            self.station[ss][stationName] = [thisTime, 1]

        return thisTime

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station[startStation][endStation][0] / self.station[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)